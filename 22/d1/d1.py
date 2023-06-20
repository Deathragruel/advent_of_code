""" First day of 2022 advent of code. Task to calculate max calories. You may
see some unnecessary f strings because i wanted each list to contain values not variables 
to avoid repetition out of personal preference. """

# create file object and initialize list to store the numbers and spaces in the file
filename = 'd1.txt'
number_list = []

# File opened, list converted into line-by-line string list, looped to convert each to integer
# and add that to a list.
with open(filename, 'r') as f:
    list = f.readlines()
    for element in list:
        try:
            number = int(element)
        except ValueError:
            space = element
            number_list.append(space)
        else:
            number_list.append(f"{number}")

# List initialized to hold each elf's total calories.
added_numbers = []

# Using totalling algorithm and conditional to get list with total calory value of each elf
total = 0
for element in number_list:
    if element != space:
        total += int(element)

    if element == space:
        added_numbers.append(int(f"{total}"))
        total = 0
        continue

# greatest calory found, respective elf is 1+index because index starts at 0
greatest_calories = max(added_numbers)
print(f"Elf {added_numbers.index(greatest_calories) + 1} has {greatest_calories} (greatest) calories.")