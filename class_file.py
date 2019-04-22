# create a class
class DataShell():

    # Declare a class variable family, and assign value of "DataShell"
    family = 'DataShell'

    # initialize class with self argument, identifier arguments
    def __init__(self, identifier):
        # Set identifier as instance variable of input argument
        self.identifier = identifier


# declare variable
x = 10

# instantiate DataShell
my_data_shell = DataShell(x)

# print data shell identifier
print(my_data_shell.family)

# Override the my_data_shell.family value with "NotDataShell"
my_data_shell.family = "NotDataShell"

# Print my_data_shell class variable family once again
print(my_data_shell.family)

