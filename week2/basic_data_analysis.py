import pandas as pd
import matplotlib.pyplot as plt

def analyze_column(data, column_name):
    # Convert column to numeric, setting errors to NaN for invalid entries
    numeric_data = pd.to_numeric(data[column_name], errors='coerce')
    # Drop missing or invalid values
    numeric_data = numeric_data.dropna()
    
    if numeric_data.empty:
        print(f"No valid numeric data found in column '{column_name}'.")
        return
    
    # Calculate statistics
    average = numeric_data.mean()
    maximum = numeric_data.max()
    minimum = numeric_data.min()
    
    print(f"\nStatistics for column '{column_name}':")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    
    # Optional visualization
    visualize = input("Would you like to visualize the data? (y/n): ")
    if visualize.lower() == 'y':
        plt.figure(figsize=(8, 4))
        plt.hist(numeric_data, bins=20, color='skyblue', edgecolor='black')
        plt.title(f"Histogram of {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.show()

def main():
    # Prompt user for CSV file name and load data
    csv_file_path = "C:\\Users\\User\\Desktop\\datasoftixs\\week2\\titanic_dataset.csv"
    try:
        data = pd.read_csv(csv_file_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    print("\nAvailable columns:")
    for col in data.columns:
        print(f" - {col}")
    
    # Prompt user to select a column to analyze
    column_name = input("\nEnter the column name to analyze: ")
    if column_name not in data.columns:
        print(f"Column '{column_name}' not found in the CSV file.")
        return
    
    analyze_column(data, column_name)

if __name__ == "__main__":
    main()
