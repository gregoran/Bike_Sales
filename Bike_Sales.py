import pandas as pd
import numpy as np
from pandas import DataFrame

file_path = r'C:\Users\DELL\Desktop\Statistics using Python_BikeSales\BikeSalesCleanedData.xlsx'
data = pd.read_excel(file_path)

print(data.head())

summary: DataFrame | None=data.describe(include='all')

print(summary)

# Group by Customer_Gender and calculate total Revenue and Profit
gender_revenue_profit = data.groupby('Customer_Gender').agg({
    'Revenue': 'sum',
    'Profit': 'sum'
})

print(gender_revenue_profit)


mode_cost = data['Cost'].mode()
mode_revenue = data['Revenue'].mode()

print(f"Mode Cost: {mode_cost.tolist()}")
print(f"Mode Revenue: {mode_revenue.tolist()}")
