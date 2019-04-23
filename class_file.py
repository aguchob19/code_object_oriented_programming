import numpy as np
import pandas as pd


# create a class
class DataShell:
    # Initialize class with self and dataList as arguments
    def __init__(self, filepath):
        # Set data as instance variable, and assign it the value of dataList
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)


us_life_expectancy = r'data_sets\us_life_expectancy.csv'

# Instantiate DataShell with us_life_expectancy as input argument
us_data_shell = DataShell(us_life_expectancy)

# Print df
print(us_data_shell.data_as_csv)


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
