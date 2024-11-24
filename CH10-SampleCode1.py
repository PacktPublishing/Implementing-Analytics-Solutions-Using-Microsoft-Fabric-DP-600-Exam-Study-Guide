# Basic Summary Statistics Using Pandas
# Requires Pandas installed: pip install pandas

import pandas as pd

data = pd.read_csv('dataset.csv')

# Print summary statistics
print(data.describe())

# Check data types
print(data.dtypes)


# Creating a Histogram in Python
# Requires Matplotlib installed: pip install matplotlib

import matplotlib.pyplot as plt

# Plot a histogram for the 'age' column
data['age'].hist()
plt.show()

# Detecting Anomalies with Boxplot in Python
# Requires Seaborn installed: pip install seaborn

import seaborn as sns

sns.boxplot(data['sales'])
plt.show()


# Implementing K-means Clustering in Python
# Requires Scikit-Learn installed: pip install scikit-learn

from sklearn.cluster import KMeans
import pandas as pd

# Load data
data = pd.read_csv('dataset.csv')

# Fit K-means clustering model
model = KMeans(n_clusters=3)
model.fit(data[['feature1', 'feature2']])


# Running a Spark Job in Synapse for Large Dataset
# Requires PySpark environment, e.g., Synapse or Databricks.

df = spark.read.csv('/mnt/data/large_dataset.csv')
df.show()
