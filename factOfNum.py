#time complexity = 0(n)
#space complexity = 0(1)

# number = int(input("Enter a number to find factorial: "))
# fact = 1;

# while number  >= 1:
#     fact = fact * number
#     number -= 1

# print(fact)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # recursive 

number = int(input("Enter a number to find factorial: "))
result = factorial(number)
print(result)

# here time and space complexity is o(n)

