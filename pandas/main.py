import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Introduction to Pandas - a powerful data analysis library for Python
print("PANDAS BASIC EXAMPLE\n")

# 1. Creating a DataFrame - the primary pandas data structure
print("1. Creating a DataFrame from a dictionary:")
data = {
    'Name': ['John', 'Sarah', 'Mike', 'Emma', 'David'],
    'Age': [28, 32, 25, 41, 35],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [75000, 65000, 70000, 85000, 78000],
    'Experience': [3, 5, 2, 8, 6]
}

df = pd.DataFrame(data)
print(df)
print("\n")

# 2. Basic DataFrame information
print("2. DataFrame basic information:")
print(f"Shape (rows, columns): {df.shape}")
print(f"Column names: {df.columns.tolist()}")
print("Data types:")
print(df.dtypes)
print("\n")

# 3. Basic statistics on numerical columns
print("3. Statistical summary of numerical data:")
print(df.describe())
print("\n")

# 4. Accessing and selecting data
print("4. Data selection examples:")
print("First 2 rows:")
print(df.head(2))
print("\nLast 2 rows:")
print(df.tail(2))
print("\nSelecting the 'Name' column:")
print(df['Name'])
print("\nSelecting multiple columns:")
print(df[['Name', 'Salary']])
print("\nSelecting row by index with .iloc:")
print(df.iloc[2])
print("\nSelecting row by label with .loc (using the index):")
print(df.loc[3])
print("\n")

# 5. Data filtering
print("5. Filtering data:")
print("Employees in IT department:")
it_employees = df[df['Department'] == 'IT']
print(it_employees)
print("\nEmployees with salary > 70000:")
high_salary = df[df['Salary'] > 70000]
print(high_salary)
print("\nComplex filtering (IT employees with experience > 4 years):")
experienced_it = df[(df['Department'] == 'IT') & (df['Experience'] > 4)]
print(experienced_it)
print("\n")

# 6. Adding and modifying data
print("6. Adding and modifying data:")
# Adding a new column
df['Bonus'] = df['Salary'] * 0.1
print("Added 'Bonus' column (10% of salary):")
print(df)
print("\nModifying the 'Bonus' for the IT department (15% instead):")
df.loc[df['Department'] == 'IT', 'Bonus'] = df['Salary'] * 0.15
print(df)
print("\n")

# 7. Sorting data
print("7. Sorting data:")
print("Sorted by Salary (descending):")
print(df.sort_values(by='Salary', ascending=False))
print("\nSorted by Department, then by Salary (descending):")
print(df.sort_values(by=['Department', 'Salary'], ascending=[True, False]))
print("\n")

# 8. Grouping and aggregation
print("8. Grouping and aggregation:")
print("Average salary by department:")
dept_salary = df.groupby('Department')['Salary'].mean()
print(dept_salary)
print("\nMultiple statistics by department:")
dept_stats = df.groupby('Department').agg({
    'Salary': ['mean', 'min', 'max', 'count'],
    'Age': 'mean',
    'Experience': 'mean'
})
print(dept_stats)
print("\n")

# 9. Handling missing data (creating some NA values for demonstration)
print("9. Handling missing data:")
df.loc[1, 'Experience'] = None
df.loc[3, 'Bonus'] = None
print("DataFrame with some missing values:")
print(df)
print("\nChecking for missing values:")
print(df.isna().sum())
print("\nFilling missing values:")
df_filled = df.fillna({'Experience': df['Experience'].mean(), 'Bonus': 0})
print(df_filled)
print("\n")

# 10. Simple visualization
print("10. Data visualization:")
print("Creating bar chart of average salary by department...")

plt.figure(figsize=(10, 6))
dept_salary.plot(kind='bar', color='skyblue')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary ($)')
plt.tight_layout()
plt.savefig('dept_salary_chart.png')
print("Bar chart saved as 'dept_salary_chart.png'")

# 11. Time series data example
print("\n11. Time series data example:")
# Create date range for the past year
dates = pd.date_range(end='2025-03-22', periods=12, freq='M')  # 12 months ending today
monthly_sales = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(10000, 50000, size=12),
    'Expenses': np.random.randint(8000, 30000, size=12)
})
monthly_sales['Profit'] = monthly_sales['Sales'] - monthly_sales['Expenses']
print(monthly_sales)

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['Date'], monthly_sales['Sales'], marker='o', label='Sales')
plt.plot(monthly_sales['Date'], monthly_sales['Expenses'], marker='s', label='Expenses')
plt.plot(monthly_sales['Date'], monthly_sales['Profit'], marker='^', label='Profit')
plt.title('Monthly Business Performance (Last 12 Months)')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('monthly_performance.png')
print("Time series chart saved as 'monthly_performance.png'")

print("\nPandas basic example completed! Check the output and generated charts.")