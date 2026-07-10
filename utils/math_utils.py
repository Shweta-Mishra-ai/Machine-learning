"""Mathematical utility functions for prime, pronic, narcissistic, special, and perfect number classifications."""

import math

def isprime(n: int) -> bool:
    """Check if a number is prime.
    
    A prime number is a positive integer greater than 1 that has no positive
    divisors other than 1 and itself.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def ispronic(n: int) -> bool:
    """Check if a number is pronic.
    
    A pronic number (or oblong number) is the product of two consecutive
    integers, i.e., n = x * (x + 1) for some integer x.
    """
    if n < 0:
        return False
    x = int(math.isqrt(n))
    return x * (x + 1) == n

def cube(n: float) -> float:
    """Compute the cube of a number."""
    return n ** 3

def square(n: float) -> float:
    """Compute the square of a number."""
    return n ** 2

def isArmstrong(n: int) -> bool:
    """Check if a number is an Armstrong (narcissistic) number.
    
    An Armstrong number of k digits is an integer that is equal to the sum
    of its digits each raised to the power of k.
    """
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    k = len(digits)
    return sum(d ** k for d in digits) == n

def ispositive(n: float) -> bool:
    """Check if a number is positive (greater than or equal to 0)."""
    return n >= 0

def ispalindrome(n: int) -> bool:
    """Check if an integer is a palindrome."""
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]

def factorial(n: int) -> int:
    """Compute the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

def isspecial(n: int) -> bool:
    """Check if a number is a Special (Strong) number.
    
    A Special number is one where the sum of the factorials of its digits
    is equal to the number itself (e.g., 145 = 1! + 4! + 5!).
    """
    if n < 0:
        return False
    return sum(math.factorial(int(d)) for d in str(n)) == n

def get_proper_divisors(n: int) -> list[int]:
    """Retrieve all proper positive divisors of a positive integer."""
    if n <= 0:
        return []
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def isniven(n: int) -> bool:
    """Check if a number is Niven (Harshad).
    
    A Niven number is an integer that is divisible by the sum of its digits.
    """
    if n <= 0:
        return False
    digit_sum = sum(int(d) for d in str(n))
    return n % digit_sum == 0

def isneon(n: int) -> bool:
    """Check if a number is Neon.
    
    A Neon number is an integer where the sum of the digits of its square
    is equal to the number itself (e.g., 9 -> 9^2 = 81 -> 8 + 1 = 9).
    """
    if n < 0:
        return False
    sq = n ** 2
    return sum(int(d) for d in str(sq)) == n

def ismagic(n: int) -> bool:
    """Check if a number is Magic.
    
    A Magic number is one where the recursive sum of digits equals 1.
    """
    if n <= 0:
        return False
    temp = n
    while temp >= 10:
        temp = sum(int(d) for d in str(temp))
    return temp == 1

def isevil(n: int) -> bool:
    """Check if a number is Evil.
    
    An Evil number is a non-negative integer that has an even number of 1s
    in its binary expansion.
    """
    if n < 0:
        return False
    return bin(n).count('1') % 2 == 0

def power(a: float, n: int) -> float:
    """Compute a raised to the power of n."""
    return a ** n

def isdisarium(n: int) -> bool:
    """Check if a number is Disarium.
    
    A Disarium number is one where the sum of its digits powered with their
    respective position (1-indexed) is equal to the number itself.
    """
    if n < 0:
        return False
    s = str(n)
    return sum(int(char) ** (i + 1) for i, char in enumerate(s)) == n

def isperfect(n: int) -> bool:
    """Check if a number is perfect.
    
    A perfect number is a positive integer that is equal to the sum of its
    proper positive divisors.
    """
    if n <= 1:
        return False
    return sum(get_proper_divisors(n)) == n

def fibonacci(n: int) -> list[int]:
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return []
    lst = []
    a, b = 0, 1
    for _ in range(n):
        lst.append(a)
        a, b = b, a + b
    return lst
