# Load numpy as np and pandas as pd
import numpy as np
import pandas as pd


# Create class: DataShell
class DataShell:
    # Class variable family
    family = 'DataShell'

    # Initialization method with arguments, and instance variables
    def __init__(self, name, filepath):
        self. name = name
        self.filepath = filepath


# Create class CsvDataShell, which inherits from DataShell
class CsvDataShell(DataShell):
    # Initialization method with arguments self, name, filepath
    def __init__(self, name, filepath):
        # Instance variable data
        self.data = pd.read_csv(filepath)
        # Instance variable stats
        self.stats = self.data.describe()


us_life_expectancy = r'data_sets\us_life_expectancy.csv'

# Instantiate CsvDataShell as us_data_shell, passing us_life_expectancy as argument
us_data_shell = CsvDataShell("US", us_life_expectancy)

# Print my_data_shell
print(us_data_shell.stats)