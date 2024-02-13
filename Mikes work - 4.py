"""
Beginner Problem: Write a function that searches all words in a text file and returns the sum of all integer values.

File Name: sum_of_integers.py
Name:      Michael Austin
Course:    CPTR 141
"""

def sum_of_integers(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        
    numbers = []
    current_number = ''
    
    for char in content:
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ''
    
    # Append the last number if it exists
    if current_number:
        numbers.append(int(current_number))
    
    total_sum = sum(numbers)
    return total_sum

"""Any File you want to use """
file_name = "numbers.txt"
print(
    "The sum of numbers in {} is {}".format(
        file_name, sum_of_integers(file_name)
    )
)

