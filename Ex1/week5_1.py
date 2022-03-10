import datetime
import os
import random

# That's the way


def find_files_in_directory_startwith_deep(path):
    """
    This function gets the path to a directory and return a list of files that start with the string "deep"
    :param path: - The path to the directory
    :return: List of files that start with "deep"
    """
    return [file for file in os.listdir(path) if file.startswith("deep")]


# Please write your own path!
print(find_files_in_directory_startwith_deep("C:/Users/אלישר/Desktop/Notebooks-master/week05/images"))

print("--------------------------------------")
##############################################
##############################################
# I don't have vinaigrette


def get_random_date_between(date1, date2):
    """
    The function gets 2 dates and return a random date between those dates
    :param date1: a date from the input in format "YYYY-MM-DD"
    :param date2: a date from the input in format "YYYY-MM-DD"
    :return: random date between the dates
    """
    random_number_of_days = random.randrange(abs(date1 - date2).days)
    random_date = date1 + datetime.timedelta(random_number_of_days)
    return str(random_date)


def random_date_between_2_dates(date1, date2):
    """
     The function gets 2 dates and after generate a random number between them print "I dont have vinaigrette
     if the the random date fall on monday
    :param date1: a date from the input in format "YYYY-MM-DD"
    :param date2: a date from the input in format "YYYY-MM-DD"
    :return: none
    """
    random_date = get_random_date_between(date1, date2)
    print("random date = " + random_date)
    if datetime.datetime.strptime(random_date, "%Y-%m-%d").date().isoweekday() == 2:
        print("I dont have vinaigrette")


date_1 = input("Enter a date\n")
date_2 = input("Enter a second date\n")

try:
    random_date_between_2_dates(datetime.datetime.strptime(date_1, "%Y-%m-%d").date()
                                ,datetime.datetime.strptime(date_2, "%Y-%m-%d").date())
except ValueError:
    print("Wrong format: the correct format is: YYYY-MM-DD")

#####################################################


