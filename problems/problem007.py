"""
Project Euler - Problem 7: 10 001st Prime

By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$. What is the $10\,001$st prime number?
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution():
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == 10001:
                return num
        num += 1

if __name__ == "__main__":
    print(solution())  # Answer: 104743