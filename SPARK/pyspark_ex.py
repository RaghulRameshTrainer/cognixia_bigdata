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
# df2=spark.read.csv(r"C:\spark\spark-3.0.3-bin-hadoop2.7\data\sparkdata\custs","C:\spark\spark-3.0.3-bin-hadoop2.7\data\custs1")
# print(df2.count())

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

#To check the number of partitions
print("No of Partition:",custdf.rdd.getNumPartitions())
custdf1=custdf.repartition(5)
print("No of Partition:",custdf1.rdd.getNumPartitions())

# cache and persists





