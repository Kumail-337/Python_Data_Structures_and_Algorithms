##################################### Iterative Functions ###############################

def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Start with first two numbers
    a, b = 0, 1

    # Calculate up to nth number
    for i in range(2, n + 1):
        a, b = b, a + b  # Update: a becomes b, b becomes sum

    return b

def print_fibonacci_sequence(n):
    """Prints first n Fibonacci numbers"""
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


print_fibonacci_sequence(10)  # Output: 0 1 1 2 3 5 8 13 21 34
print(fibonacci(10))  # Output: 55

##################################### Recursive Functions ###############################

def bad_fibonacci(n):
  """Return the nth Fibonacci number."""
  #print(n)
  if n <= 1:
    return n
  else:
    return bad_fibonacci(n-2) + bad_fibonacci(n-1)

def good_fibonacci(n):
  """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
  if n <= 1:
    return (n,0)
  else:
    (a, b) = good_fibonacci(n-1)
    return (a+b, a)


def print_fibonacci_recursive(n, a=0, b=1):
    """Prints first n Fibonacci numbers using recursion"""
    # Base case: stop when n reaches 0
    if n <= 0:
        print()  # Print newline at the end
        return

    # Print current Fibonacci number
    print(a, end=" ")

    # Recursive call with updated values
    print_fibonacci_recursive(n - 1, b, a + b)

print(bad_fibonacci(10))
print(good_fibonacci(10))
print_fibonacci_sequence(10)