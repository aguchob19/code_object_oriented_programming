# Load numpy as np and pandas as pd
import numpy as np
import pandas as pd


# Create class: DataShell
class DataShell:
    def __init__(self, inputFile):
        self.file = inputFile


us_life_expectancy = r'data_sets\us_life_expectancy.csv'

# Instantiate DataShell as my_data_shell
my_data_shell = DataShell(us_life_expectancy)

# Print my_data_shell
print(my_data_shell)