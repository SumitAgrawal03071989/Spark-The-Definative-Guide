# Chapter 4. Structured API Overview

The majority of the Structured APIs apply to both batch and streaming computation.

## DataFrames and Datasets

* Spark has two notions of structured collections: DataFrames and Datasets.
* DataFrames and Datasets are (distributed) table-like collections with well-defined rows and columns.
* Tables and views are basically the same thing as DataFrames. We just execute SQL against them instead of DataFrame code.

## Schemas

* A schema defines the column names and types of a DataFrame.
* You can define schemas manually or read a schema from a data source (often called schema on read).

## Overview of structured Spark Types

* Spark is effectively a programming language of its own. Internally, Spark uses an engine called Catalyst that maintains its own type information through the planning and processing of work

```
# in Python
df = spark.range(500).toDF("number")
df.select(df["number"] + 10)
```

## Dataframes vs DataSets

* Dataframes ( unTyped - not actually ) , spark maintains type of Dataframes completely and only checks whether those types line up to those specified in the schema at runtime.
* Datasets are only available to Java Virtual Machine (JVM)–based languages (Scala and Java) and we specify types with case classes or Java beans.
* DataFrames are simply Datasets of Type Row
* The “Row” type is Spark’s internal representation of its optimized in-memory format for computation. This format makes for highly specialized and efficient computation because rather than using JVM types, which can cause high garbage-collection and object instantiation costs, Spark can operate on its own internal format without incurring any of those costs.

## Columns 
* Columns represent a simple type like an integer or string, a complex type like an array or map, or a null value.
* Simply think of column on table 

## Rows 
* A row is nothing more than a record of data. Each record in a DataFrame must be of type Row, as we can see when we collect the following DataFrames. We can create these rows manually from SQL, from Resilient Distributed Datasets (RDDs), from data sources, or manually from scratch. Here, we create one by using a range:

```
# in Python
spark.range(2).collect()
```



