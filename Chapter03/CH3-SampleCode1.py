# Data Processing with Azure Databricks
# This script should be run within a Databricks notebook or PySpark environment.

from pyspark.sql import SparkSession

# Initialize a SparkSession for data processing
spark = SparkSession.builder.appName("Data Processing").getOrCreate()

# Load sample data from a CSV file; replace '/path/to/your/data.csv' with the actual file path
df = spark.read.csv('/path/to/your/data.csv', header=True, inferSchema=True)

# Perform a simple data transformation: select two columns and filter rows
transformed_df = df.select("Column1", "Column2").filter("Column2 > 1000")

# Show the transformed data
transformed_df.show()
