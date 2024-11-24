import pandas as pd

# Load large dataset
data = pd.read_csv('sales_data.csv')

# Partition data based on a date column
data['partitioned_date'] = pd.to_datetime(data['sale_date']).dt.to_period('M')
monthly_data = data.groupby('partitioned_date')

# Save each partition as a separate file
for date, partition in monthly_data:
    partition.to_csv(f'sales_data_{date}.csv', index=False)


from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ParallelProcessing").getOrCreate()

# Load data and perform transformations
df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)
df = df.filter(df["amount"] > 0).groupBy("category").sum("amount")

# Write optimized data
df.write.csv("optimized_sales_data.csv", header=True)


import pandas as pd

# Load extracted raw sales data
data = pd.read_csv('raw_sales_data.csv')

# Add a calculated 'sales_tax' column
data['sales_tax'] = data['sales_amount'] * 0.1

# Save the final transformed data
data.to_csv('final_transformed_sales_data.csv', index=False)
