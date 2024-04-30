import random


for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    filename = letter + '.txt'  
    with open(filename, 'w') as file:
        random_number = random.randint(1, 100)
        file.write(str(random_number))


with open('summary.txt', 'w') as summary_file:
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        filename = letter + '.txt'  
        with open(filename, 'r') as file:
            number = file.read().strip()
            summary_file.write(f'{filename}: {number}\n')
