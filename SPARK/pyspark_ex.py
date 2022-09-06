from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType,IntegerType
spark=SparkSession.builder.appName('Cognixia Training').getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

print(""" 1. Create DataFrame (rdd->DF , reading a file)""")
'''
rdd=spark.sparkContext.textFile(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custs")
rdd1=rdd.map(lambda x:x.split(",")).filter(lambda x:len(x)==5)
custSchema=StructType([ \
    StructField("custId", IntegerType(), True), \
    StructField("fname",StringType(),True) ,\
    StructField("lname",StringType(),True),\
    StructField("age",IntegerType(), True),\
    StructField("profession",StringType(),True)
])

df=spark.createDataFrame(rdd,custSchema)
df.show()
'''
df=spark.read.csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custs")
print(df.count())
df1=spark.read.csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custs*")
print(df1.count())
#E df2=spark.read.csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custs","C:\spark\spark-3.0.3-bin-hadoop2.7\data\custs1")
#E print(df2.count())

print("""2.********************TRANSFORM*******************""")
custSchema=StructType([ \
    StructField("custId", IntegerType(), True), \
    StructField("fname",StringType(),True) ,\
    StructField("lname",StringType(),True),\
    StructField("age",IntegerType(), True),\
    StructField("profession",StringType(),True)
])
custdf=spark.read.option("mode","dropmalformed").csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custs",
                                                                        schema=custSchema)
custdf.show()

# custdf.cache()
# #To check the number of partitions
# print("No of Partition:",custdf.rdd.getNumPartitions())
# custdf1=custdf.repartition(5)
# print("No of Partition:",custdf1.rdd.getNumPartitions())
#
# # cache and persists
# custdf2=custdf.repartition(10)


# custdf.unpersist()
#
# from pyspark import StorageLevel
# #custdf.persist(storagelevel.DISK_ONLY)
# custdf.persist(StorageLevel.MEMORY_AND_DISK)
# custdf.unpersist()

custdf.createOrReplaceTempView("customer")
suspenseDf=spark.sql("""SELECT * FROM customer 
            WHERE custid is null 
            OR fname is null
            OR lname is null
            OR age is null
            OR profession is null""")
print("Total number of records with null : ", suspenseDf.count())


validdata=spark.sql("""SELECT * FROM customer 
            WHERE custid is not null 
            AND fname is not null
            AND lname is not null
            AND age is not null
            AND profession is not null""")
print("Total number of records without null : ", validdata.count())

#custdf1=custdf.na.drop()
#print("Total number of records without null :: ", custdf1.count())

filleddf=spark.sql(""" SELECT custid, fname, lname ,age, case 
                    WHEN profession is null THEN 'UNKNOWN'
                    ELSE profession
                    END as profession
                    FROM customer""")
filleddf.createOrReplaceTempView("updated_customer")
spark.sql("""SELECT * FROM updated_customer WHERE profession='UNKNOWN'""").show(100)
from pyspark.sql.functions import col
finaldf=custdf.na.fill({'profession':"MISSING"})
finaldf.createOrReplaceTempView("cust_tbl1")
# spark.sql("""SELECT count(1) FROM cust_tbl1
#             WHERE profession='MISSING'""").show()

updtdf=spark.sql("""SELECT custid,fname,lname,age, CASE 
                            WHEN profession='Computer hardware engineer' THEN 'ENGG'
                            WHEN profession='Childcare worker' THEN 'DAY CARE'
                            WHEN profession='Financial analyst' THEN 'Auditor'
                            ELSE profession 
                            END AS profession
                            FROM cust_tbl1""")
updtdf.createOrReplaceTempView("cust_updt_tbl")
# spark.sql("""SELECT count(1) FROM cust_updt_tbl
#             WHERE profession IN ('ENGG','DAY CARE','Auditor')""").show()

# mychange={'Computer hardware engineer':'ENGG','Childcare worker':'DAY CARE',
#           'Financial analyst':'Auditor'}
#
# rdf=finaldf.replace(mychange,subset=['profession'])
# rdf.createOrReplaceTempView("mytable")
# spark.sql("""SELECT count(1) FROM mytable
#             WHERE profession in ('ENGG','DAY CARE','Auditor')""").show()

# uniquedf=finaldf.distinct()
# print("Total number of unique records :",uniquedf.count())

