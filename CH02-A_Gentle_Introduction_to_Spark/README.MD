# Chapter 2. A Gentle Introduction to Spark

## Spark’s Basic Architecture
Single machine or group of machine is not enough to achieve large data computation / processing.
Spark with resource manager like yarn is framework to achive above

## Spark Applications
Spark employs a cluster manager that keeps track of the resources available.
The driver process is responsible for executing the driver program’s commands across the executors to complete a given task.

The executors are responsible for actually carrying out the work that the driver assigns them

## Starting Spark


### The SparkSession
You control your Spark Application through a driver process called the SparkSession.

### DataFrames
A DataFrame is the most common Structured API and simply represents a table of data with rows and columns.
You can think of a DataFrame as a spreadsheet with named columns. Figure 2-3 illustrates the fundamental difference: a spreadsheet sits on one computer in one specific location, whereas a Spark DataFrame can span thousands of computers.

### Partitions
To allow every executor to perform work in parallel, Spark breaks up the data into chunks called partitions. A partition is a collection of rows that sit on one physical machine in your cluster.

### Transformations
In Spark, the core data structures are immutable, meaning they cannot be changed after they’re created.
2 types of transformations
1. narrow dependencies
	Each input partition will contribute to only one output partition
2. wide dependencies
	Input partitions contributing to many output partitions

### Lazy Evaluation
Lazy evaulation means that Spark will wait until the very last moment to execute the graph of computation instructions.

### Actions
Transformations allow us to build up our logical transformation plan. To trigger the computation, we run an action.


