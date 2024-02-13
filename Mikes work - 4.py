"""
Beginner Problem: Write a function that searches all words in a text file and returns the sum of all integer values.

File Name: sum_of_integers.py
Name:      Michael Austin
Course:    CPTR 141
"""
"""Any File you want to use """
file_name = "numbers.txt"

print(
    "The sum of numbers in {} is {}".format(
        file_name, sum_of_integers.sum_of_integers(file_name)
    )
)

def sum_of_integers(file_name):
    with open(file_name, "r") as file:
        rows = file.read().splitlines()

    total_sum = 0
    for r in rows:
        data = r.split(" ")
        for d in data:
            try:
                num = int(d)
                total_sum += num 
            except Exception as e:
                continue
    return total_sum
