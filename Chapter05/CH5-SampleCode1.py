import pandas as pd
from datetime import datetime

def batch_copy(source_file, target_file):
    data = pd.read_csv(source_file)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    data.to_csv(f"{target_file}_{timestamp}.csv", index=False)

# Example usage
batch_copy("data_file.csv", "backup_data_file")


import pyodbc

def real_time_replication(source_conn_str, target_conn_str, query):
    source_conn = pyodbc.connect(source_conn_str)
    target_conn = pyodbc.connect(target_conn_str)
    source_cursor = source_conn.cursor()
    target_cursor = target_conn.cursor()
    source_cursor.execute(query)
    data = source_cursor.fetchall()

    for row in data:
        target_cursor.execute("INSERT INTO target_table VALUES (?, ?)", row)

    target_conn.commit()
    source_conn.close()
    target_conn.close()

# Example usage
source_connection_string = "DRIVER={SQL Server};SERVER=source_server;DATABASE=source_db;UID=user;PWD=password"
target_connection_string = "DRIVER={SQL Server};SERVER=target_server;DATABASE=target_db;UID=user;PWD=password"
real_time_replication(source_connection_string, target_connection_string, "SELECT * FROM source_table")


import pandas as pd
from datetime import datetime, timedelta

def incremental_copy(source_file, target_file, last_sync):
    data = pd.read_csv(source_file)
    updated_data = data[data['last_modified'] > last_sync]
    updated_data.to_csv(target_file, index=False)

# Example usage
last_sync_time = datetime.now() - timedelta(days=1)
incremental_copy("data_file.csv", "updated_data_file.csv", last_sync_time.strftime('%Y-%m-%d %H:%M:%S'))


import hashlib

def calculate_checksum(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Example usage
print(calculate_checksum("data_file.csv"))


from calculate_checksum import calculate_checksum

def validate_data(source_path, target_path):
    source_checksum = calculate_checksum(source_path)
    target_checksum = calculate_checksum(target_path)
    return source_checksum == target_checksum

# Example usage
if validate_data("source_data.csv", "target_data.csv"):
    print("Data integrity verified.")
else:
    print("Data integrity check failed.")


import pandas as pd

def partition_data(source_file, chunk_size):
    data = pd.read_csv(source_file, chunksize=chunk_size)
    for i, chunk in enumerate(data):
        chunk.to_csv(f"data_chunk_{i}.csv", index=False)

# Example usage
partition_data("large_data_file.csv", 10000)



import pandas as pd

def convert_format(source_file, target_file):
    data = pd.read_csv(source_file)
    data.to_json(target_file, orient='records', lines=True)

# Example usage
convert_format("data_file.csv", "data_file.json")



import pandas as pd

def aggregate_data(source_file, target_file):
    data = pd.read_csv(source_file)
    aggregated_data = data.groupby("category").sum()
    aggregated_data.to_csv(target_file)

# Example usage
aggregate_data("data_file.csv", "aggregated_data.csv")



import pandas as pd

def transform_data(source_file, target_file, transformations):
    data = pd.read_csv(source_file)
    for transform in transformations:
        data = transform(data)
    data.to_csv(target_file, index=False)

# Define transformations
def convert_date_format(data):
    data['date'] = pd.to_datetime(data['date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
    return data

def normalize_column(data, column):
    data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())
    return data

transformations = [convert_date_format, lambda data: normalize_column(data, 'value')]

# Example usage
transform_data("source_data.csv", "transformed_data.csv", transformations)
