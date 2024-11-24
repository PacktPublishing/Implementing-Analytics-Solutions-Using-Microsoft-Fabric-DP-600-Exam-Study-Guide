import pandas as pd

def transform_sales_data(raw_data_file, transformed_data_file):
    data = pd.read_csv(raw_data_file)
    # Standardize date format
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    # Fill missing values by forward fill
    data.fillna(method='ffill', inplace=True)
    # Normalize numerical values
    data['sales'] = (data['sales'] - data['sales'].min()) / (data['sales'].max() - data['sales'].min())
    data.to_csv(transformed_data_file, index=False)

# Example usage
transform_sales_data('raw_sales_data.csv', 'transformed_sales_data.csv')




import pandas as pd

data = pd.read_csv('raw_data.csv')
# Remove duplicates
data = data.drop_duplicates()
# Handle missing values by forward filling
data = data.fillna(method='ffill')
# Save the cleaned data
data.to_csv('cleaned_data.csv', index=False)



from sklearn.preprocessing import StandardScaler
import pandas as pd

data = pd.read_csv('raw_data.csv')
# Standardize the data
scaler = StandardScaler()
data[['numerical_column']] = scaler.fit_transform(data[['numerical_column']])
# Save the standardized data
data.to_csv('standardized_data.csv', index=False)


from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = pd.read_csv('raw_data.csv')
scaler = MinMaxScaler()
data[['numerical_column']] = scaler.fit_transform(data[['numerical_column']])
data.to_csv('minmax_scaled_data.csv', index=False)


import pandas as pd

raw_data = {
    'customer_id': [1, 2, 3],
    'purchase_amount': [100, 200, 150],
    'purchase_date': ['2023-01-01', '2023-01-02', '2023-01-03']
}
df = pd.DataFrame(raw_data)
df.to_csv('structured_data.csv', index=False)



