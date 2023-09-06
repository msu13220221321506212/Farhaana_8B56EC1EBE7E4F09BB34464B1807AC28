# 1.1 Implement a recursive function to calculate the factorial of a given number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")