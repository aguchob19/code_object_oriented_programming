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

