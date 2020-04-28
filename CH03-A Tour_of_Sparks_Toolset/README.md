# Chapter 4. Structured API Overview

## Running Production Applications
You can write applications in any of Spark’s supported languages and then submit them for execution.

## Datasets: Type-Safe Structured APIs
The Dataset API is not available in Python and R, because those languages are dynamically typed.
The Dataset API gives users the ability to assign a Java/Scala class to the records within a DataFrame and manipulate it as a collection of typed objects, similar to a Java ArrayList or Scala Seq.
The APIs available on Datasets are type-safe, meaning that you cannot accidentally view the objects in a Dataset as being of another class than the class you put in initially.
Datasets ( post manipulations if any ) can be converted to dataframes

## Structured Streaming
Structured Streaming is a high-level API for stream processing that became production-ready in Spark 2.2. With Structured Streaming, you can take the same operations that you perform in batch mode using Spark’s structured APIs and run them in a streaming fashion.

## Lower-Level APIs
Spark includes a number of lower-level primitives to allow for arbitrary Java and Python object manipulation via Resilient Distributed Datasets (RDDs).
RDDs are lower level than DataFrames because they reveal physical execution characteristics (like partitions) to end users.
As end users, you shouldn’t need to use RDDs much in order to perform many tasks unless you’re maintaining older Spark code. There are basically no instances in modern Spark, for which you should be using RDDs instead of the structured APIs beyond manipulating some very raw unprocessed and unstructured data.  