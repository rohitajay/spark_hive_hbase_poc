from pyspark.sql import SparkSession

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, HiveContext

# SparkContext.setSystemProperty("hive.metastore.uris", "thrift://localhost:9083", conf=SparkConf())
sparkSession = (SparkSession
                .builder
                .appName('integration-pyspark-hive').config("hive.metastore.uris", "thrift://localhost:9083", conf=SparkConf())\
                .enableHiveSupport()
                .getOrCreate())

data = [('First', 1), ('Second', 2), ('Third', 3), ('Fourth', 4), ('Fifth', 5)]

df = sparkSession.createDataFrame(data)

# Write into Hive
# df.write.saveAsTable("example")

# df_load = sparkSession.sql('create database abc')
sparkSession.sql("show databases").show()
# df_load.show()
# print(df_load.show())

# sparkSession.sql('show databases').show()
#

print("hello world")