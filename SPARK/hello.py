from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Deloite Project").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df=spark.read.csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\usdata.csv",
                  header="true",inferSchema="true")
#df.printSchema()
#df.show(500,False)
# df1=spark.read.load(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\transactions.xml",
#                     format="xml"
#                     )
#df1.show()
from pyspark.sql.types import StructType,StructField,StringType,FloatType, IntegerType
salesSchema=StructType([\
    StructField("productId",StringType(),True),\
    StructField("productName",StringType(), True),\
    StructField("stdCost",FloatType(),True),\
    StructField("stdPrice",FloatType(), True),\
    StructField("effDt",StringType(),True),\
    StructField("dt",StringType(),True)
    ])
salesDF=spark.read.load(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\sales_woh.csv",
                    format="csv",
                    schema=salesSchema
                    )
#salesDF.printSchema()
#salesDF.na.drop(subset=['productId','productName']).show()
# salesDF.na.fill({'productId':'SUPA111',
#                  'productName':'SURF EXCL'}).show()
#salesDF.na.replace({'01-01-2019':'05-09-2022'}).show()
finalDF=salesDF.na.replace(['01-03-2019 00:00','02-03-2019 00:00'],['05-09-2022 10:10','06-09-2022 11:11'],'effDt').\
    replace({'01-01-2019':'05-09-2022'})
#finalDF.show()  #DSL
#salesDF.show()
#print(salesDF.count())
custSchema=StructType([ \
    StructField("custName",StringType(),True) ,\
    StructField("city",StringType(),True),\
    StructField("age",IntegerType(), True),\
    StructField("salary",IntegerType(),True)
])
custDF=spark.read.load(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custdata.txt",
                       format="csv",
                       schema=custSchema)

#custDF.show()
custDF1=spark.read.load(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custdata.txt",
                       format="csv").toDF('Name','City','Age','Salary')

rdd=spark.sparkContext.parallelize([
    (1000,'Raghul','Ramesh','Chennai',10000),
    (1001,'Siva','Rajesh','Bangalore',20000),
    (1002,'Charanya','Srini','Hyderabad',30000)
])

#df2=spark.createDataFrame(rdd,schema=['custid','fname','lname','city','amount'])
#df2.show()
#salesDF.show()
from pyspark.sql.functions import col,lit
sDF=salesDF.withColumn("finalCost",col("stdCost") * 10)
sDF1=sDF.withColumn("company",lit("Deloitte"))
sDF2=sDF1.withColumn("finalPrice",col("stdPrice") * 100)
# sDF3=sDF2.drop('stdCost')
# sDFfinal=sDF3.drop('stdPrice')
sDFfinal=sDF2.drop(*('stdCost','stdPrice'))
#sDFfinal.show()
# sDFfinal.withColumnRenamed("productId","ID")\
#     .withColumnRenamed("productName","Name").show()

# mode
# DROPMALFORMED, PERMISSIVE, FAILFAST
custSchema1=StructType([ \
    StructField("custID",IntegerType(),True) ,\
    StructField("custName",StringType(),True),\
    StructField("age",IntegerType(), True),\
    StructField("city",StringType(),True)
])

# custDF=spark.read.option("mode","DROPMALFORMED").\
#     csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custdata.txt",
#                       schema=custSchema1).\
#     toDF('empid','empname','age','location')
custDF=spark.read.option("mode","PERMISSIVE").\
    csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custdata.txt",
                      schema=custSchema1).\
    toDF('empid','empname','age','location')
# custDF=spark.read.option("mode","FAILFAST").\
#     csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custdata.txt",
#                       schema=custSchema1).\
#     toDF('empid','empname','age','location')
###################################################################################
################ CRAETE A TABLE ON TOP OF DF ######################################
###################################################################################
custDF.createOrReplaceTempView("customer")
suspenseDF=spark.sql(""" SELECT * FROM customer
                        WHERE empid is NULL or 
                            empname is NULL or
                            age is NULL or
                            location is NULL"""
                     )
#spark.sql("SELECT * FROM customer WHERE location='Chennai'").show()
#suspenseDF.write.mode("overwrite").format("csv").save(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\output\suspense_records.csv")
