import numpy as np
import pandas as pd


# create a class
class DataShell:
    # Initialize class with self and dataList as arguments
    def __init__(self, filepath):
        # Set data as instance variable, and assign it the value of dataList
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)

    # Define method rename_column, with arguments self, column_name, and new_column_name
    def rename_column(self, column_name, new_column_name):
        self.data_as_csv.columns = self.data_as_csv.columns.str.replace(column_name, new_column_name)

    # Define get_stats method, with argument self
    def get_stats(self):
        return self.data_as_csv.describe()

us_life_expectancy = r'data_sets\us_life_expectancy.csv'

# Instantiate DataShell with us_life_expectancy as input argument
us_data_shell = DataShell(us_life_expectancy)

# Define method rename_column, with arguments self, column_name, and new_column_name
print(us_data_shell.get_stats())