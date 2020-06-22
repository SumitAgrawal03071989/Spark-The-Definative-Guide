## RDD vs DataFrames vs DataSets.
https://databricks.com/blog/2016/07/14/a-tale-of-three-apache-spark-apis-rdds-dataframes-and-datasets.html

## Databricks Spark Knowledge Base
https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/index.html

## How to add column to DataFrame.
DF.WithColumn("NameOFColumn", Expression)

## How to Drop column 
DF.drop("Column Name")

## Can I run two applications in single spark script.
ReSearch: Here the question might be weather we can run more than one job in one application.
Here Job is nothing but when we call any actions post completing our transformations.
Jobs at start of application if not utilising complete cluster then next jobs in queue can be started.
Default is FIFO Scheduler.
FIFO Scheduler and Fair Schedular.

FIFO, Allocate resources based on Queue, If first is not utilising all resources then allocate it to second.
FAIR, Allocate resoirces to all jobs in equal fashion, So that small jobs could start.



## GroupbyKey vs ReduceByKey

## How many stages would be created 
All operations before shuffle would be part of single Stage.

## How many task would be created.
1) Number of Task depends on number of partitions in data.
2) for Range of numbers = Tasks = number of Core in machine / cluster.


## Define the functions of Spark Core.
Serving as the base engine, Spark Core performs various important functions like memory management, monitoring jobs, providing fault-tolerance, job scheduling, and interaction with storage systems.

## What is RDD Lineage?	
Spark does not support data replication in memory and thus, if any data is lost, it is rebuild using RDD lineage. RDD lineage is a process that reconstructs lost data partitions. The best thing about this is that RDDs always remember how to build from other datasets.


## What is Spark Context and Spark Session
Spark Context.
https://sparkbyexamples.com/spark/spark-sparkcontext/


=!=


## Partitions in Spark.
Hash Partition.
Range Partition.
https://medium.com/@goyalsaurabh66/partitioning-in-apache-spark-7efece460f7c


## Choose between groupByKey and reduceByKey.
https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html


## monotonically_increasing_id
we can also add a unique ID to each row by using the function monotonically_increasing_id. This function generates a unique value for each row, starting with 0:
```
// in Scala
import org.apache.spark.sql.functions.monotonically_increasing_id
df.select(monotonically_increasing_id()).show(2)

```

## String manipulations.
initcap function.


## if a column is declared as null while defining schema, what would happen if it discovere null while reading the column.


## Aggregation
RelationalGroupedDataset


## While reading JSON, check multiline and other catches.

## Spark partitioning and bucketing, what is spark managed tables?

## Various spark modes available ( local , cluster , ....)


## Explore all options in this.
```

SELECT [ALL|DISTINCT] named_expression[, named_expression, ...]
    FROM relation[, relation, ...]
    [lateral_view[, lateral_view, ...]]
    [WHERE boolean_expression]
    [aggregation [HAVING boolean_expression]]
    [ORDER BY sort_expressions]
    [CLUSTER BY expressions]
    [DISTRIBUTE BY expressions]
    [SORT BY sort_expressions]
    [WINDOW named_window[, WINDOW named_window, ...]]
    [LIMIT num_rows]

named_expression:
    : expression [AS alias]

relation:
    | join_relation
    | (table_name|query|relation) [sample] [AS alias]
    : VALUES (expressions)[, (expressions), ...]
          [AS (column_name[, column_name, ...])]

expressions:
    : expression[, expression, ...]

sort_expressions:
    : expression [ASC|DESC][, expression [ASC|DESC], ...]

```

## DataSets.
What we can do with Datasets and not with DataFrame.
Grooping in case of dataSets

## Pair RDDs to System Commands

## How to check existing partitions in Spark
getNumPartitions


## Kryo Serialization









## Spark Vectors. ( This is something related to machine learning libs, Does not make sense to cover now)
* Sparce vector
* Dense vector




