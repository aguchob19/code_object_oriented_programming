# create a class
class DataShell():
    # initialize class with self argument
    def __init__(self, identifier, data):
        # Set identifier and data as instance variables, assigning value of input arguments
        self.identifier = identifier
        self.data = data


# declare variable
x = 10
y = [1, 2, 3, 4, 5]

# instantiate DataShell
my_data_shell = DataShell(x, y)

# print data shell identifier
print(my_data_shell.identifier)

# print data shell data
print(my_data_shell.data)
