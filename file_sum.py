# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/05/2023
# Description: Write a function named file_sum that takes as a parameter the name
# of a text file that contains a list of numbers, one to a line. The function
# should sum the values in the file and write the sum (just that number) to a
# text file named sum.txt.

def file_sum(filename):
    """Finds the sum of a set of numbers."""
    sum = 0
    with open(filename) as outfile:
        for num in outfile:
            sum += float(num)
    with open("sum.txt", "w") as outfile:
        outfile.write(str(sum) + "\n")


if __name__ == '__main__':
    file_sum("numbers.txt")
