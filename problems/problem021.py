"""
Project Euler - Problem 21: Amicable Numbers

Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$). If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers. For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$. Evaluate the sum of all the amicable numbers under $10000$.
"""

def sum_of_divisors(n):
    """Return the sum of proper divisors of n."""
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors)

def solution():
    """Return the sum of all amicable numbers under 10000."""
    amicable_numbers = set()
    for a in range(1, 10000):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
    return sum(amicable_numbers)

if __name__ == "__main__":
    print(solution())  # Answer: 31626