import numpy as np


# Array filled of with zeros

zero_array = np.zeros((4,3))
print(zero_array)



# Array filled of with ones

ones_array = np.ones((4, 3))
print(ones_array)



# Array filled of with numbers from 0 to 11

array_elevens = np.arange(12)
shaped_elevens = array_elevens.reshape((4, 3))
print(shaped_elevens)