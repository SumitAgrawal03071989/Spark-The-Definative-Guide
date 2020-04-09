# Chapter 21. Structured Streaming Basics

## Input Sources

Structured Streaming supports several input sources for reading in a streaming fashion. As of Spark 2.2, the supported input sources are as follows:

1. Apache Kafka 0.10
2. Files on a distributed file system like HDFS or S3 (Spark will continuously read new files in a directory)
3. A socket source for testing

## Sinks
Just as sources allow you to get data into Structured Streaming, sinks specify the destination for the result set of that stream. Sinks and the execution engine are also responsible for reliably tracking the exact progress of data processing. Here are the supported output sinks as of Spark 2.2

1. Apache Kafka 0.10
2. Almost any file format
3. A foreach sink for running arbitary computation on the output records
4. A console sink for testing
5. A memory sink for debugging

## Output Modes
1. Append (only add new records to the output sink)
2. Update (update changed records in place)
3. Complete (rewrite the full output)

One important detail is that certain queries, and certain sinks, only support certain output modes, as we will discuss later in the book. For example, suppose that your job is just performing a map on a stream. The output data will grow indefinitely as new records arrive, so it would not make sense to use Complete mode, which requires writing all the data to a new file at once. In contrast, if you are doing an aggregation into a limited number of keys, Complete and Update modes would make sense, but Append would not, because the values of some keys’ need to be updated over time.

## Triggers
Spark also supports triggers based on processing time (only look for new data at a fixed interval). In the future, other types of triggers may also be supported.

## Event-Time Processing
Structured Streaming also has support for event-time processing (i.e., processing data based on timestamps included in the record that may arrive out of order)

## EVENT-TIME DATA
Event-time means time fields that are embedded in your data. This means that rather than processing data according to the time it reaches your system, you process it according to the time that it was generated, even if records arrive out of order at the streaming application due to slow uploads or network delays. 

## WATERMARKS.
Watermarks are a feature of streaming systems that allow you to specify how late they expect to see data in event time. 

# Structured Streaming in Action
Let’s get to an applied example of how you might use Structured Streaming. For our examples, we’re going to be working with the Heterogeneity Human Activity Recognition Dataset. The data consists of smartphone and smartwatch sensor readings from a variety of devices—specifically, the accelerometer and gyroscope, sampled at the highest possible frequency supported by the devices. Readings from these sensors were recorded while users performed activities like biking, sitting, standing, walking, and so on. There are several different smartphones and smartwatches used, and nine total users.


/Users/sumitagrawal/PSpace/Projects/spark/Spark-The-Definitive-Guide-master/data/retail-data/by-day/2010-12-01.csv