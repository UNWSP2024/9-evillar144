# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

import random
question = int(input("How many random numbers do you want (up to 1000): "))
if question > 1000:
    print("YOU CANT DO THAT DUMBASS")
else:
    with open('text.txt', 'w') as file:
        for _ in range(question):
            num = random.randint(1, 500)
            file.write(f"{num}\n")
        print(f"{question} random numbers have been written to 'text.txt'.")
