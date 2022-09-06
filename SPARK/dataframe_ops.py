from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType,IntegerType
spark=SparkSession.builder.appName('Cognixia Training').getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
nums=spark.sparkContext.parallelize([(1,'Chennai'),
                                     (2,'Bangalore'),
                                     (3,'Hyderabad'),
                                     (4,'Pune'),
                                     (5,'New Delhi')])
val citySchema=StructType(Array(
    StructField("ID", IntegerType,false), \
    StructField("CITY",StringType,false) \
    ))
#df=spark.createDataFrame(nums)
#df.show()
# df=nums.toDF(['ID','CITY'])
# df.show()

# ------------------DF and DS ---------------------
