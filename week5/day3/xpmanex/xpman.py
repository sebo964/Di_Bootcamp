# Exercise 1 : Built-In Functions

# Instructions

# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.
"""This is a simple doc string"""

num_user = input(f"Enter a number: ")

num_int = int(num_user)
num_abs = abs(num_int)

print(f"Absolute value of {num_user} is {num_abs}")


# 🌟 Exercise 2: Currencies

# Instructions


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if self.currency == other.currency:
            return self.amount + other.amount
        else:
            raise TypeError("Cannot add between Currency type <dollar> and <shekel>")
            # raise ("Cannot add between Currency type <dollar> and <shekel>")

    # Your code starts HERE


# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
c1 = Currency("dollar", 5)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)
c2 = Currency("dollar", 10)

print(c1)

c1 += c2

print(c1)

d1 = c3 + c1
print(d1)


# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
