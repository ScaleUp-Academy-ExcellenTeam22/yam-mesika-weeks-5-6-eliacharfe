import math
import random
import string


names = ['Yam', 'Gal', 'Orpaz', 'Aviram']
greek_names = list(map(lambda name: name + 'os', names))
print(f"Greek names: {greek_names}")
print("--------------------------------------------")
################################################

numbers = [1, 2, 3, 4, 5]
square_list = [number * number for number in numbers]
print(f"square list (from list): {square_list}")

square_range = [number * number for number in range(1, 6)]
print(f"square list (from range): {square_range}")
print("--------------------------------------------")
#################################################

list_of_tuples = [(number, number+1) for number in range(1, 6)]
print(f"list_of_tuples (from range): {list_of_tuples}")
print("--------------------------------------------")
#################################################
names = ['Margaret Thatcher', 'Karl Marx', "Ze'ev Jabotinsky", 'Bertrand Russell', 'Fidel Castro']
long_names = list(filter(lambda long_name: len(long_name) > 12, names))
print(f"long names: {long_names}")
print("---------------------------------------------")
######################################################
# Handle sqrt

CHARACTERS = f'.{string.digits}{string.ascii_letters}'
WEIGHTS = [1] * len(f'.{string.digits}') + [0.05] * len(string.ascii_letters)


def generate_size(length):
    return ''.join(random.choices(CHARACTERS, weights=WEIGHTS, k=length))


def generate_closet(closet_size=20, shoe_size=4):
    return [generate_size(shoe_size) for _ in range(closet_size)]


def is_float(my_string):
    """
    Check if the string represent a number (float) if so return true else false
    :param my_string: A string to check
    :return: True if can be converted to float number else false
    """
    try:
        return float(my_string)
    except ValueError:
        return False


def organize_closet(list_closet):
    """
    Gets a list of strings representing sizes of clothes and returns a list of the square root of the strings
    that represent a number.
    Possible input: ['Area51', '303', '2038', 'f00b4r', '314.1']
    The output: [17.41, 45.14, 17.72]
    :param list_closet: A list of strings representing sizes of clothes
    :return: A list of the square root of the strings that represent a number (after rounding to 2 nums after point)
    """
    return [round(math.sqrt(float(size_closet)), 2) for size_closet in list_closet if size_closet.isnumeric()
            or is_float(size_closet)]


lst_closet = generate_closet(10)
print(f"before: {lst_closet}")
print(f"after: {organize_closet(lst_closet)}")

print(f"before: {['100', '25.0', '12a', 'mEoW', '0']}")
print(f"after: {organize_closet(['100', '25.0', '12a', 'mEoW', '0'])}")

print(f"before: {['Area51', '303', '2038', 'f00b4r', '314.1']}")
print(f"after: {organize_closet(['Area51', '303', '2038', 'f00b4r', '314.1'])}")

print("-----------------------------------------")
#################################################

counter = len({num for num in range(0, 1000) if (num % 7) == 0 and (num % 3) == 0})
print(f"number of numbers (under 1000) that can be divided by 3 and by 7 is: {counter}")

print("-----------------------------------------")
#################################################

dice_options_gen_expression = (
    (die1, die2, die3)
    for die1 in range(1, 7)
    for die2 in range(1, 7)
    for die3 in range(1, 7)
)

print(f"Generator expression: {list(dice_options_gen_expression)}")


def dice_generator_function():
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            for die3 in range(1, 7):
                yield die1, die2, die3


print(f"Generator function: {list(dice_generator_function())}")

print("----------------------------------------")
################################################

print(f"Generator expression (set): {set(dice_options_gen_expression)}")
print(f"Generator function (set): {set(dice_generator_function())}")

print("----------------------------------------")
################################################
# Be in peace


def words_length(sentence):
    """
    Function that get a sentence of words and returns a list of the length of the words in it
    :param sentence: The sentence
    :return: A list of the length of the words in the sentence sent
    """
    return [len(x) for x in sentence.split()]


print("The list of the words length: " + str(words_length("Toto, I've a feeling we're not in Kansas anymore")))
print("-----------------------------------------------")
#######################################################
# א אוהל, פה זה פייתון


def get_letters():
    """
    A function that returns a list of all lowercase/uppercase letters
    :return: A list of all lowercase/uppercase letters
    """
    return [chr(letter_low) for letter_low in range(ord('a'), ord('z')+1)] +\
           [chr(letter_up) for letter_up in range(ord('A'), ord('Z')+1)]


print(get_letters())
print("------------------------------------------------")
########################################################
# Long cat is long


def count_words(txt):
    """
    The function gets a text, first cuts all characters that are not letters or whitespaces, then returns
    a dictionary of the words (as keys) and their length (as value)
    :param txt: The text sent
    :return: A dictionary of the words (as keys) and their length (as value)
    """
    my_clean_text = ''.join(ch for ch in txt if ch.isalnum() or ch.isspace())
    return {word: len(word) for word in my_clean_text.split()}


text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

print(count_words(text))
print("--------------------------------------------------")
##########################################################


def full_names(firsts_names, lasts_names, min_length=0):
    """
    Gets a list of first names and a list of last names and an optional parameter min_length and return
    a list of all combinations of first names with last names that are greater or equal to the min_length
    if passed (by default min_length is 0), that after will turn each first/last name to uppercase at
    the first letter
    :param firsts_names: A list of first names
    :param lasts_names: A list of last names
    :param min_length: (optional) The full names that are greater than this parameter
    :return: List of all full names
    """
    return [first[0].upper() + first[1:] + " " + last[0].upper() + last[1:]
            for first in firsts_names for last in lasts_names
            if len(first + ' ' + last) >= min_length]


first_names = ['avi', 'moshe', 'yaakov']
last_names = ['cohen', 'levi', 'mizrahi']

print(full_names(first_names, last_names))
print(full_names(first_names, last_names, 10))

print("-------------------------------------------")
###################################################









