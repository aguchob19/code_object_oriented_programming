import numpy as np


# Create function that returns the average of an integer list
# num_list = [1,2,3]
def average_numbers(num_list):
    avg = sum(num_list) / float(len(num_list))
    return avg

# my_matrix = [[1,2,3,4], [5,6,7,8]]
# Create a function that returns a NumPy array
def return_array(my_matrix):
    array = np.array(my_matrix, dtype = float)
    return array