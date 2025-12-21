##################################### Iterative Function ###############################

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2,n + 1):
            result *= i
        return result

print(factorial(5))

##################################### Recursive Function ###############################

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(recursive_factorial(5))