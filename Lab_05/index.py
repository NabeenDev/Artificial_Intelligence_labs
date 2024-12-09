# Q No 1

print("Write a program that uses a loop to print numbers from 1 to 10:")
for i in range(1, 11):
    print("The Number is: ", i)


# Q no 2
# print(
#     "Write a function that calculates the sum of all numbers up to a given number using a loop."
# )

print("The Sum of the Numbers 1 to 10")
sum = 0
for i in range(1, 10):
    sum += i

print("The Sum of all Numbers:",sum)


# Q No 4: Write a function that takes a list of numbers and prints only the even numbers.

for i in range(1, 21):
    if i % 2 == 0:
        print("The Only Even Numbers is: ", i)



for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

# Number of rows for the star pattern
rows = 5

# Outer loop for each row
for i in range(1, rows + 1):
    # Print spaces to align stars to the center
    for j in range(rows - i):
        print(" ", end="")
    # Print stars in each row
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line after each row
    print()