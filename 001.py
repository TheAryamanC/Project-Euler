import time

### Problem 1

## Problem statement:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

## Solution 1:
# Perhaps the first way that an inexperienced mathematician would solve this problem is by creating three lists
# One list of all the multiples of 3 below 1000, one list of all the multiples of 5 below 1000, and one list of all the multiples of 15 below 1000
# Then, the sum of all the multiples of 3 or 5 below 1000 would be the sum of the first two lists minus the sum of the third list
# Yes, this will result in the correct answer, but to explain why it is not the most efficient way to solve this problem, let's look at how long it takes to do this

print("Solution 1: Three lists up to 1000")
start = time.time_ns()
multiples_of_3 = [i for i in range(3, 1000, 3)]
multiples_of_5 = [i for i in range(5, 1000, 5)]
multiples_of_15 = [i for i in range(15, 1000, 15)]
sum_of_multiples = sum(multiples_of_3) + sum(multiples_of_5) - sum(multiples_of_15)
print("Sum of multiples of 3 or 5 below 1000:", sum_of_multiples)
end = time.time_ns()
print("Time taken (ns):", end - start) # ~1000000 ns
print()

# For small numbers like 1000, this method is quite fast for a computer
# But we want to push the limits of computation, so let's try a far larger number
# But let's try some large number like 100 million, let's see how long it takes

print("Solution 1: Three lists up to 100000000")
start = time.time()
multiples_of_3 = [i for i in range(3, 100000000) if i % 3 == 0]
multiples_of_5 = [i for i in range(5, 100000000) if i % 5 == 0]
multiples_of_15 = [i for i in range(15, 100000000) if i % 15 == 0]
sum_of_multiples = sum(multiples_of_3) + sum(multiples_of_5) - sum(multiples_of_15)
print("Sum of multiples of 3 or 5 below 1000:", sum_of_multiples)
end = time.time()
print("Time taken:", end - start) # ~30 seconds
print()

# I have also tried this with 1 billion, but it took too long to compute
# In short, this method probably isn't going to cut it for large numbers
# I understand that some people are probably asking "what's the point" since we already got the answer
# But my goal is to find better ways to solve these problems, and adopt a better mindset for solving problems in general

## Solution 2:
# A slightly more experienced mathematician would probably realize that there is no need to create three lists
# Instead, we can just iterate through all the numbers below 1000, and check if they are multiples of 3 or 5
# This solves the problem of having to check for multiples of 15
# It also solves the problem of having to store all the multiples in memory, which will save up considerable time
# Let's see how long this method takes

print("Solution 2: Iterating through all numbers up to 1000")
start = time.time_ns()
sum_of_multiples = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
print("Sum of multiples of 3 or 5 below 1000:", sum_of_multiples)
end = time.time_ns()
print("Time taken (ns):", end - start) # ~1000000 ns
print()

# Interestingly, this takes about the same time as the first method for multiple up to 1000
# But let's try a larger number like 100 million

print("Solution 2: Iterating through all numbers up to 100000000")
start = time.time()
sum_of_multiples = sum([i for i in range(100000000) if i % 3 == 0 or i % 5 == 0])
print("Sum of multiples of 3 or 5 below 10000000:", sum_of_multiples)
end = time.time()
print("Time taken:", end - start) # ~17 seconds
print()

# This method is definitely faster than the first method for large numbers - it took about half the time
# Now here is where the tradeoff between computation speed and code readability comes in
# The next part of the problem is generalizability - how can we make this code work for any number, not just 1000 or 100 million?
# And how can we make it work for any two numbers, not just 3 and 5?