from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

df1 = spark.readStream.format("kafka")\
  .option("kafka.bootstrap.servers", "localhost:9092")\
  .option("subscribe", "topic2")\
  .load()

print("********************************************************************************")



df1.selectExpr("topic", "CAST(key AS STRING)", "CAST(value AS STRING)")\
  .writeStream\
  .format("kafka")\
  .option("kafka.bootstrap.servers", "localhost:9092")\
  .option("checkpointLocation", "/Users/sumitagrawal/PSpace/Projects/spark/CH21-Structured_Streaming_Basics/Spark/checkpoint/")\
  .option("topic", "topic3")\
  .start()


print("*********************************Started Writing***********************************************")


testQuery = df1.selectExpr("topic", "CAST(key AS STRING)", "CAST(value AS STRING)")\
	.writeStream.queryName("test_table")\
  .format("memory").outputMode("append")\
  .start()

from time import sleep
for x in range(20):
    spark.sql("SELECT * FROM test_table").show()
    sleep(1)
