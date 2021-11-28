"""
👋 😬

Section 1 
  Q1 : replicate factorial function without built-in  


Options:
    (a) iterative
    (b) recursion like in fractal

"""


num = int(input("Enter a number: "))  # -> int

def recursive_factorial(n):
    """recursive method"""

    if n == 1:
        return n
    elif n < 1:
        return "NA"
    else:
        return n * recursive_factorial(n - 1)


def iterative_factorial(n):
    """iterative method"""

    factor = 1
    if n >= 1:
        for i in range(1, n + 1):
            factor = factor * i
    return factor


print("iterative method :", iterative_factorial(num))
print("recursive method : ", recursive_factorial(num))
