from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("Data Processing").getOrCreate()

# Load sample data (replace '/path/to/your/data.csv' with your data file path)
df = spark.read.csv('/path/to/your/data.csv', header=True, inferSchema=True)

# Perform a simple data transformation
transformed_df = df.select("Column1", "Column2").filter("Column2 > 1000")

# Show the transformed data
transformed_df.show()
