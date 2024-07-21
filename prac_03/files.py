"""
CP1404/CP5632 - Practical
"""

# Question 1: Write name to file using open and close
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Question 2: Read name from file and print greeting using open and close
in_file = open("name.txt", "r")
name = in_file.read().strip()  # Using read() and strip() to remove newlines
in_file.close()
print(f"Hi {name}!")

# Question 3: Read and add first two numbers from file using with
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())  # Using readline() to get the first line
    second_number = int(in_file.readline())  # Using readline() again to get the second line

total = first_number + second_number
print(total)  # Should print 59

# Question 4: Read and add all numbers from file using with and for loop
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:  # Using for line in file to iterate through lines
        total += int(line)
    print(total)