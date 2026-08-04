"""
Project Euler - Problem 17: Number Letter Counts

If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total. If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used? NOTE: Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$ letters and $115$ (one hundred and fifteen) contains $20$ letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def solution():
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    total = 0
    for i in range(1, 1001):
        if i < 10:
            total += len(ones[i])
        elif i < 20:
            total += len(teens[i - 10])
        elif i < 100:
            total += len(tens[i // 10]) + (len(ones[i % 10]) if i % 10 != 0 else 0)
        elif i < 1000:
            total += len(ones[i // 100]) + len('hundred') + (len('and') + len(tens[(i % 100) // 10]) + (len(ones[(i % 100) % 10]) if (i % 100) % 10 != 0 else 0) if i % 100 != 0 else 0)
        else:
            total += len('onethousand')
    return total

if __name__ == "__main__":
    print(solution())  # Answer: 20818  # Answer: 21124