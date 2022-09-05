from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Deloite Project").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df=spark.read.option("mode","DROPMALFORMED").csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\usdata.csv",
                  header="true",inferSchema="true")
print("2.Please find below for the schema informations:")
print("="*50)
df.printSchema()
print('*'*100)
df1=df.drop('web')
from pyspark.sql.functions import col
df2=df1.withColumn("current_age",col("age")+1).drop("age")
df3=df2.withColumnRenamed("company_name","company")
df3.createOrReplaceTempView("us_customer")
df_50above=spark.sql("SELECT * FROM us_customer WHERE current_age>=50")
print("Total number of customer with age 50 and above is :", df_50above.count())
df_50below=spark.sql("SELECT count(1) FROM us_customer WHERE current_age<50")
print("Total number of customer with age below 50 is :", df_50below.collect())
print("No of customer from each state wise below:")
print("\n=========================================")
spark.sql(""" SELECT state, count(1)
                FROM us_customer
                GROUP BY state
                ORDER BY count(1) DESC
""").show(100)
