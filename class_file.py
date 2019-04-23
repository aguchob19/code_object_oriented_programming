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


us_life_expectancy = r'data_sets\us_life_expectancy.csv'

# Instantiate DataShell with us_life_expectancy as input argument
us_data_shell = DataShell(us_life_expectancy)

# Define method rename_column, with arguments self, column_name, and new_column_name
print(us_data_shell.data_as_csv.dtypes)

# Rename your objects column 'code' to 'country_code'
us_data_shell.rename_column('code', 'country_code')

# Again, print the datatype of your object's data_as_csv attribute
print(us_data_shell.data_as_csv.dtypes)

# # Define method that returns data: show
# def show(self):
#     # return
#     return self.data
#
#
# # Define method that prints average of data: avg
# def avg(self):
#     avg = sum(self.data) / float(len(self.data))
#     # returnd
#     return avg
