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


# Define class TsvDataShell
class TsvDataShell(DataShell):
    # Initialization method with arguments self, name, filepath
    def __init__(self, name, filepath):
        # Instance variable data
        self.data = pd.read_csv(filepath, sep='\t')
        # Instance variable stats
        self.stats = self.data.describe()


us_life_expectancy = r'data_sets\us_life_expectancy.csv'

# Instantiate CsvDataShell as us_data_shell, print us_data_shell.stats
us_data_shell = CsvDataShell("US", us_life_expectancy)
print(us_data_shell.stats)

france_life_expectancy = r'data_sets\france_life_expectancy.txt'

# Instantiate TsvDataShell as france_data_shell, print france_data_shell.stats
france_data_shell = TsvDataShell("France", france_life_expectancy)
print(france_data_shell.stats)