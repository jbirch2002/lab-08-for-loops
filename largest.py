largest_number = 0

for i in range(4):
    number = int(input("Number please.... "))

    if number > largest_number:
        largest_number = number

print("The largest number is", largest_number)