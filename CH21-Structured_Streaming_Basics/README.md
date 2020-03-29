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

