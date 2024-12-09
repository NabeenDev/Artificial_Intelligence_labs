# task # 1
# Write a Python function that takes a number as input and returns the sum of its digits.
# take user input
num = int(input("Enter the number: "))

# define a function that take one input and add them
def checksum(a):
    sum = 0
    for i in range(1, a + 1):
        sum += i
    return f"the sum of its digits {sum}"


# checksum(num)
# # function call
result1 = checksum(num)
# your desire result
print(result1)

# task # 2
# Write a Python function that takes a sentence as input and returns the number of words in it.

userInput = input("Enter the Sentence: ")


# print(userInput)
def CalSentenceLength(x):
    return len(x)


result2 = CalSentenceLength(userInput)
print(f"the length of the sentence is {result2}")

# task # 3
# Write a Python function that takes an integer and returns whether the number is even or odd.


num1 = int(input("Enter the number: "))


def checkEvenOrOdd(x):
    if x % 2 == 0:
        return f"{x} is even Number"
    else:
        return f"{x} is odd Number"


result3 = checkEvenOrOdd(num1)
print(result3)