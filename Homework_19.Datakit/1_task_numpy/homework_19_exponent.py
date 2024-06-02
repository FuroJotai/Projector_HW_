import numpy as np

def calculate_x(x):
    result = []
    for num in x:
        f_x = np.exp(-num)
        result.append(f_x)

    return np.array(result)   

array_of_x = np.arange(-10, 11) 

array_of_func = calculate_x(array_of_x)

for x, fx in zip(array_of_x, array_of_func):
    print(f'x = {x}, F(x) = {fx}')