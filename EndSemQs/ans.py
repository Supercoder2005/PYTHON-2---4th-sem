import pandas as pd 
data = pd.read_csv('F:\\PYTHON 2 - 4th sem\\EndSemQs\\transactions.csv')
print(data)

# drop row with anything missing value or NaN value 
data_new = data.dropna()
print(data_new)

# function check if the date and amount is valid 
def is_valid_date(date_str):
    try:
        pd.to_datetime(date_str,format='%Y-%m-%d')
        return True 
    except:
        return False
def is_valid_amount(amount_str):
    try:
        float(amount_str)
        return True 
    except:
        return False 
    
data_new = data[data['Date'].apply(is_valid_date)]
data_new = data[data['Amount'].apply(is_valid_amount)]

# remove rows with status = failed 
new_data = data[data['Status']!= 'Failed']
print(new_data)

#convert 'Date' column to datetime format
new_data['Date'] = pd.to_datetime(new_data['Date'],format='%Y-%m-%d')
print(new_data)

#total spending amount per category , consider only where status = completed 
data1 = data[data['Status']=='Completed']
print(data1)
total_spending = data1.groupby('Category')['Amount'].sum()
print(total_spending)

#total spending amount per customer , status = completed
data2 = data[data['Status']=='Completed']
total_spending_per_customer = data2.groupby('CustomerID')['Amount'].sum()
print(total_spending_per_customer)

#top customers by total spending in descending order
top_customers = data2.groupby('CustomerID')['Amount'].sum()
top_customers = top_customers.sort_values(ascending = False)
print(top_customers)