import numpy as np

array_of_x, array_of_func = np.arange(1, 101), 2 * np.arange(1, 101) ** 2 + 5

print("\n".join([f'x = {x} F(x) = {f_x}' for x, f_x in zip(array_of_x, array_of_func)]))