# create a class
class DataShell():
    # initialize class with self argument
    def __init__(self, integerInput):
        # Set data as instance variable, and assign the value of integerInput
        self.data = integerInput


# declare variable
x = 10

# instantiate DataShell
my_data_shell = DataShell(x)

# print data shel
print(my_data_shell.data)
