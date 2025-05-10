import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Set page configuration
st.set_page_config(
    page_title="Pandas Data Visualization",
    page_icon="📊",
    layout="wide"
)

# Main title
st.title("📊 Pandas Data Visualization Dashboard")
st.write("This interactive dashboard visualizes sample data using pandas and Streamlit.")

# Create employee data
@st.cache_data
def create_employee_data():
    data = {
        'Name': ['John', 'Sarah', 'Mike', 'Emma', 'David'],
        'Age': [28, 32, 25, 41, 35],
        'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
        'Salary': [75000, 65000, 70000, 85000, 78000],
        'Experience': [3, 5, 2, 8, 6]
    }
    df = pd.DataFrame(data)
    # Add bonus column
    df['Bonus'] = df['Salary'] * 0.1
    # Modify bonus for IT department
    df.loc[df['Department'] == 'IT', 'Bonus'] = df['Salary'] * 0.15
    # Add some missing values for demonstration
    df.loc[1, 'Experience'] = None
    df.loc[3, 'Bonus'] = None
    return df

# Create time series data
@st.cache_data
def create_time_series_data():
    # Create date range for the past year
    end_date = datetime.date(2025, 3, 22)
    dates = pd.date_range(end=end_date, periods=12, freq='M')
    np.random.seed(42)  # For reproducibility
    monthly_sales = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randint(10000, 50000, size=12),
        'Expenses': np.random.randint(8000, 30000, size=12)
    })
    monthly_sales['Profit'] = monthly_sales['Sales'] - monthly_sales['Expenses']
    return monthly_sales

# Load data
df = create_employee_data()
monthly_sales = create_time_series_data()

# Create tabs
tab1, tab2, tab3 = st.tabs(["Employee Data", "Department Analysis", "Time Series"])

# Tab 1: Employee Data
with tab1:
    st.header("Employee Dataset")
    
    # Interactive filters
    st.subheader("Data Filters")
    col1, col2 = st.columns(2)
    
    with col1:
        departments = st.multiselect(
            "Select Departments",
            options=df['Department'].unique(),
            default=df['Department'].unique()
        )
    
    with col2:
        min_salary = st.slider(
            "Minimum Salary",
            min_value=int(df['Salary'].min()),
            max_value=int(df['Salary'].max()),
            value=int(df['Salary'].min())
        )
    
    # Filter data based on selections
    filtered_df = df[df['Department'].isin(departments) & (df['Salary'] >= min_salary)]
    
    # Display filtered dataframe
    st.subheader("Filtered Employee Data")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Display statistics
    st.subheader("Statistical Summary")
    st.dataframe(filtered_df.describe(), use_container_width=True)
    
    # Missing values information
    st.subheader("Missing Values")
    st.write("Number of missing values in each column:")
    st.dataframe(pd.DataFrame(filtered_df.isna().sum(), columns=["Count"]), use_container_width=True)

# Tab 2: Department Analysis
with tab2:
    st.header("Department Analysis")
    
    # Average salary by department
    st.subheader("Average Salary by Department")
    dept_salary = df.groupby('Department')['Salary'].mean().reset_index()
    
    # Display as bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(dept_salary['Department'], dept_salary['Salary'], color='skyblue')
    ax.set_title('Average Salary by Department')
    ax.set_xlabel('Department')
    ax.set_ylabel('Average Salary ($)')
    st.pyplot(fig)
    
    # Multiple statistics by department
    st.subheader("Department Statistics")
    dept_stats = df.groupby('Department').agg({
        'Salary': ['mean', 'min', 'max', 'count'],
        'Age': 'mean',
        'Experience': 'mean'
    })
    st.dataframe(dept_stats, use_container_width=True)
    
    # Department comparison
    st.subheader("Department Comparison")
    selected_depts = st.multiselect(
        "Select Departments to Compare",
        options=df['Department'].unique(),
        default=list(df['Department'].unique())[:2]
    )
    
    if selected_depts:
        comparison_df = df[df['Department'].isin(selected_depts)]
        fig, ax = plt.subplots(figsize=(12, 6))
        
        for dept in selected_depts:
            dept_data = comparison_df[comparison_df['Department'] == dept]
            ax.scatter(dept_data['Experience'], dept_data['Salary'], label=dept, s=100, alpha=0.7)
        
        ax.set_title('Salary vs Experience by Department')
        ax.set_xlabel('Years of Experience')
        ax.set_ylabel('Salary ($)')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)
        st.pyplot(fig)

# Tab 3: Time Series
with tab3:
    st.header("Monthly Business Performance")
    
    # Display time series data
    st.subheader("Monthly Sales Data")
    st.dataframe(monthly_sales, use_container_width=True)
    
    # Plot time series
    st.subheader("Sales, Expenses, and Profit Over Time")
    
    # Select metrics to display
    metrics = st.multiselect(
        "Select Metrics to Display",
        options=["Sales", "Expenses", "Profit"],
        default=["Sales", "Profit"]
    )
    
    if metrics:
        fig, ax = plt.subplots(figsize=(12, 6))
        
        if "Sales" in metrics:
            ax.plot(monthly_sales['Date'], monthly_sales['Sales'], marker='o', linestyle='-', label='Sales')
        
        if "Expenses" in metrics:
            ax.plot(monthly_sales['Date'], monthly_sales['Expenses'], marker='s', linestyle='--', label='Expenses')
        
        if "Profit" in metrics:
            ax.plot(monthly_sales['Date'], monthly_sales['Profit'], marker='^', linestyle='-.', label='Profit')
        
        ax.set_title('Monthly Business Performance (Last 12 Months)')
        ax.set_xlabel('Month')
        ax.set_ylabel('Amount ($)')
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
    
    # Rolling averages
    st.subheader("Rolling Averages")
    window_size = st.slider("Select Window Size for Rolling Average", min_value=2, max_value=6, value=3)
    
    rolling_df = monthly_sales.copy()
    for col in ["Sales", "Expenses", "Profit"]:
        rolling_df[f"{col} (Rolling Avg)"] = rolling_df[col].rolling(window=window_size).mean()
    
    # Drop NA values from rolling calculation
    rolling_df = rolling_df.dropna()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(rolling_df['Date'], rolling_df['Sales'], 'o-', label='Sales', alpha=0.3)
    ax.plot(rolling_df['Date'], rolling_df['Sales (Rolling Avg)'], 'o-', label=f'Sales ({window_size}-month avg)', linewidth=3)
    ax.set_title(f'Sales with {window_size}-Month Rolling Average')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount ($)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Pandas Data Visualization Demo - Created with Streamlit")