import time

# Closing math


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calc(num1, num2, math_sign):
    dictionary = {
        '+': add(num1, num2),
        '-': subtract(num1, num2),
        '*': multiply(num1, num2),
        '/': divide(num1, num2)
    }
    return dictionary[math_sign]


print(calc(5, 2, '+'))
print(calc(5, 2, '-'))
print(calc(5, 2, '*'))
print(calc(5, 2, '/'))
print("-------------------------------------------")
#######################################################
# From here to here


def square(number):
    return number ** 2


def apply(func, iterable):
    for item in iterable:
        yield func(item)


square_check = apply(square, [5, -1, 6, -8, 0])
print(tuple(square_check) == (25, 1, 36, 64, 0))
print("------------------------------------------------")
###########################################################
# map


def generate_first_names(lst):
    return map(lambda name:  name.split(' ', 1)[0], lst)


for first_name in generate_first_names(['Bob Smith', 'Alice Johnson', 'Ali Baba']):
    print(first_name)

print("----------------------------------------------")
##########################################################
# filter


def generate_only_polyndromes(lst):
    return filter(lambda word: word == word[::-1], lst)


for polyndrome in generate_only_polyndromes(['abba', 'bob', 'week6_2', '1234', 'python', 'ArqqrA', 'WoW']):
    print(polyndrome)

print("---------------------------------------------------")
###########################################################

closet = [
    {'name': 'Peter', 'year_of_birth': 1927, 'gender': 'Male'},
    {'name': 'Edmund', 'year_of_birth': 1930, 'gender': 'Male'},
    {'name': 'Lucy', 'year_of_birth': 1932, 'gender': 'Female'},
    {'name': 'Susan', 'year_of_birth': 1928, 'gender': 'Female'},
    {'name': 'Jadis', 'year_of_birth': 0, 'gender': 'Female'},
]

print(sorted(closet, key=lambda d: d['name'][-1]))

print("---------------------------------------------------")
###########################################################
# Personally adjusted filter


def my_filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item


for polyndrome in my_filter(lambda word: word == word[::-1], ['abba', 'bob', 'week6_2', '1234', 'python', 'ArqqrA', 'WoW']):
    print(polyndrome)

print("--------------------------------------------")
####################################################
# Stay ? positive


def get_positive_numbers(inp):
    return list(filter(lambda x: x != ',' and (int(x) % 2) == 0, inp))


print(get_positive_numbers(input("Enter a serie of numbers separated by ',': \n")))

print("--------------------------------------------------------\n")
###############################################################
# 2000 running


def timer(f, *args):
    start_time = time.time()
    f(args)
    return time.time() - start_time


print(timer(print, "Hello"))
print(timer(zip, [1, 2, 3], [4, 5, 6]))
#print(timer("Hi {name}".format, name="Bug"))



