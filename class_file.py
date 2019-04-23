import numpy as np
import pandas as pd


# create a class
class DataShell:
    # Initialize class with self and dataList as arguments
    def __init__(self, inputFile):
        # Set data as instance variable, and assign it the value of dataList
        self.file = inputFile

    # Define generate_csv method, with self argument
    def generate_csv(self):
        self.data_as_csv = pd.read_csv(self.file)
        return self.data_as_csv


us_life_expectancy = r'data_sets\us_life_expectancy.csv'

# Instantiate DataShell with us_life_expectancy as input argument
data_shell = DataShell(us_life_expectancy)

# Call data_shell's generate_csv method, assign it to df
df = data_shell.generate_csv()

# Print df
print(df)


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
