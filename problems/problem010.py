"""
Project Euler - Problem 10: Summation of Primes

The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$. Find the sum of all the primes below two million.
"""

def solution():
    limit = 2000000
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime numbers
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return sum(num for num, is_prime in enumerate(sieve) if is_prime)

if __name__ == "__main__":
    print(solution())  # Answer: 142913828922