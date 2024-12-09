## Lab no 5

## Assignments no 5

Q No 1: Write a program that uses a loop to print numbers from 1 to 10?

# Input Code:

    print("Write a program that uses a loop to print numbers from 1 to 10:")
    for i in range(1, 11):
        print("The Number is: ", i)

# Output Code:

    Write a program that uses a loop to print numbers from 1 to 10:
    The Number is:  1
    The Number is:  2
    The Number is:  3
    The Number is:  4
    The Number is:  5
    The Number is:  6
    The Number is:  7
    The Number is:  8
    The Number is:  9
    The Number is:  10

Q No 2: Write a function that calculates the sum of all numbers up to a given number using a loop.

# Input Code:

    print("The Sum of the Numbers 1 to 10")
    sum = 0
    for i in range(1, 10):
        sum += i

    print("The Sum of all Numbers:",sum)

# Output Code:

    The Sum of the Numbers 1 to 10
    The Sum of all Numbers: 45

Q No 3: Write code using loops and nested loops to create star pattern

# Input Code:

    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
                for k in range(2 * i - 1):
                    print("*", end="")
            print()

#  Output Code:
            *
           ***
          *****
         *******
        *********
        
Q No 4: Write a function that takes a list of numbers and prints only the even numbers.

# Input Code:

    Print("Those are Even Number The Range in 1 to 21")
    for i in range(1, 21):
        if i % 2 == 0:
            print("The Only Even Numbers is: ", i)

# Output Code:

    Those are Even Number The Range in 1 to 21
    The Only Even Numbers is:  2
    The Only Even Numbers is:  4
    The Only Even Numbers is:  6
    The Only Even Numbers is:  8
    The Only Even Numbers is:  10
    The Only Even Numbers is:  12
    The Only Even Numbers is:  14
    The Only Even Numbers is:  16
    The Only Even Numbers is:  18
    The Only Even Numbers is:  20