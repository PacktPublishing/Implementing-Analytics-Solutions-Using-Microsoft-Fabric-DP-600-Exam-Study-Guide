import pandas as pd
import json

with open('nested_data.json') as f:
    data = json.load(f)
df = pd.json_normalize(data)
df.to_csv('flattened_data.csv', index=False)


import pandas as pd

data = pd.read_csv('time_series_data.csv', parse_dates=['timestamp'], index_col='timestamp')
monthly_data = data.resample('M').mean()
data['rolling_mean'] = data['value'].rolling(window=7).mean()
data.to_csv('transformed_time_series_data.csv')


from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("OptimizeTransformation").getOrCreate()
df = spark.read.csv("raw_data.csv", header=True, inferSchema=True)
df = df.filter(df["amount"] > 0).groupBy("category").sum("amount")
df.write.csv("optimized_data.csv", header=True)



import pandas as pd

def check_data_integrity(data_file):
    data = pd.read_csv(data_file)
    if data.isnull().sum().any():
        raise ValueError("Data contains missing values")
    if data.duplicated().any():
        raise ValueError("Data contains duplicate records")
    print("Data integrity check passed")

# Example usage
check_data_integrity('transformed_data.csv')
