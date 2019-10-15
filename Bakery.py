# Sam Cole
# this goes through two lists and finds the average if both and the maximum and the minimum
Cookies = []
Candy = []


def cookie_input():  # gives the user the oppurtunity to fill the list
    m = 1
    for i in range(0, 6):
        month = int(input(f"Please enter number of cookies for month {m}"))
        Cookies.append(month)
        m = m + 1


def candy_input():  # gives the user the oppurtunity to fill the lsit
    m = 1
    for i in range(0, 6):
        month = int(input(f"Please enter number of candies for month {m}"))
        Candy.append(month)
        m = m + 1


def average_cookie_sale():  # finds the average between all of the months
    total = 0
    for cookie in Cookies:
        total = cookie + total

    average = total / 6
    return average


def average_candy_sale():  # finds the average between all of the months
    total = 0
    for candies in Candy:
        total = candies + total

    average = total / 6
    return average


def max_cookie():  # finds the max cookie sale month
    big = 0
    for cookie in Cookies:
        if cookie > big:
            big = cookie
    print(big)


def max_candy():  # finds the max candy sale month
    big = 0
    for candies in Candy:
        if candies > big:
            big = candies
    print(big)


def min_cookie():  # finds the min cookie sale month
    small = 1000
    for cookie in Cookies:
        if small > cookie:
            small = cookie
    print(small)


def min_candy():  # finds the min candy sale month
    small = 1000
    for candies in Candy:
        if small > candies:
            small = candies
    print(small)


cookie_input()
candy_input()
average_cookie_sale()
average_candy_sale()
max_cookie()
max_candy()
min_cookie()
min_candy()
if average_cookie_sale() > average_candy_sale():  # determines which product is more popular
    print(f"The cookies are more popular at the bakery")
else:
    print(f"The candies are more popular at the bakery")
