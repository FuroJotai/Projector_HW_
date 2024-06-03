import numpy as np

array_of_x, array_of_func = np.arange(-10, 11), np.exp(np.arange(-10, 11))

print("\n".join([f'x = {x} F(x) = {f_x}' for x, f_x in zip(array_of_x, array_of_func)]))