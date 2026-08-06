"""
Project Euler - Problem 19: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself. 1 Jan 1900 was a Monday. Thirty days has September, April, June and November. All the rest have thirty-one, Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine. A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400. How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def solution():
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def days_in_month(month, year):
        if month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if is_leap_year(year) else 28
        else:
            return 31

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = 0  # 1 Jan 1900 was a Monday
    sunday_count = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            if days_of_week[day_index] == "Sunday":
                sunday_count += 1
            day_index = (day_index + days_in_month(month, year)) % 7

    return sunday_count

if __name__ == "__main__":
    print(solution())  # Answer: 172  # Answer: 171