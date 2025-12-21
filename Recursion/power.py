##################################### Iterative Function ###############################

def power(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        result = x
        for i in range(n - 1):
            result *= x
        return result

print(power(2,8))

##################################### Recursive Functions ###############################

def slow_power(x,n):
    if n == 0:
        return 1
    else:
        return x * slow_power(x,n - 1)

def fast_power(x,n):
    if n == 0:
        return 1
    else:
        partial = fast_power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

print(slow_power(2,8))
print(fast_power(2,8))