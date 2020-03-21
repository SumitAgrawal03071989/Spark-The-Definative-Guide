# Chapter 5. Basic Structured Operations

* a DataFrame consists of a series of records (like rows in a table), that are of type Row, and a number of columns (like columns in a spreadsheet) that represent a computation expression that can be performed on each individual record in the Dataset.
* Schemas define the name as well as the type of data in each column
* Partitioning of the DataFrame defines the layout of the DataFrame or Dataset’s physical distribution across the cluster.

## Schemas
* A schema defines the column names and types of a DataFrame.
* We can either let a data source define the schema (called schema-on-read) or we can define it explicitly ourselves.

* A schema is a StructType made up of a number of fields, StructFields, that have a name, type, a Boolean flag which specifies whether that column can contain missing or null values,
* Schemas can contain other StructTypes (Spark’s complex types).

## DataFrame Transformations

* We can add rows or columns
* We can remove rows or columns
* We can transform a row into a column (or vice versa)
* We can change the order of rows based on the values in columns






