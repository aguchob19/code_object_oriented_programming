# Load numpy as np and pandas as pd
import numpy as np
import pandas as pd


# Create class: DataShell
class DataShell:
    def __init__(self, inputFile):
        self.file = inputFile


# Create class CsvDataShell, which inherits from DataShell
class CsvDataShell(DataShell):
    def __init__(self, inputFile):
        self.inputFile = inputFile
        self.data = pd.read_csv(inputFile)

us_life_expectancy = r'data_sets\us_life_expectancy.csv'

# Instantiate CsvDataShell as us_data_shell, passing us_life_expectancy as argument
us_data_shell = CsvDataShell(us_life_expectancy)

# Print my_data_shell
print(us_data_shell.data)