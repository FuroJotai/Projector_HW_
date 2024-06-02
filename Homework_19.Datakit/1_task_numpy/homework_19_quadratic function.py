import numpy as np


def calculate_f(x):
    result = []
    for num in x:
        f_x = 2 * num ** 2 + 5
        result.append(f_x)

    return np.array(result) 


array_of_x = np.arange(1, 101)

array_of_func = calculate_f(array_of_x)

for x, f_x in zip(array_of_x, array_of_func):
    print(f' x = {x}, F(x) = {f_x}' )

print(array_of_x)