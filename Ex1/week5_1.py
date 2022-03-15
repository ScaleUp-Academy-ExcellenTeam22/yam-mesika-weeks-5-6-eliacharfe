import datetime
import os
import random

# That's the way


def find_files_with_deep_prefix(directory_path):
    """
    This function gets the path to a directory and return a list of files that start with the string "deep"
    :return: List of files that start with "deep"
    """
    return [file for file in os.listdir(directory_path) if file.startswith("deep")]


# I don't have vinaigrette


def get_random_date_between(first_date, second_date):
    """
    The function gets 2 dates and return a random date between those dates.
    """
    random_number_of_days = random.randrange(abs(first_date - second_date).days)
    random_date_between_dates = first_date + datetime.timedelta(random_number_of_days)
    return random_date_between_dates


def random_date_between_dates_check_if_monday(first_input_date, second_input_date):
    """
     The function gets 2 dates and after generate a random number between then print "I dont have
     vinaigrette" if the the random date fall on monday.
    """
    try:
        first_date = datetime.datetime.strptime(first_input_date, "%Y-%m-%d").date()
        second_date = datetime.datetime.strptime(second_input_date, "%Y-%m-%d").date()
    except ValueError:
        print("Wrong format: the correct format is: YYYY-MM-DD")
        return
    random_date = get_random_date_between(first_date, second_date)
    print("Random date between is: " + str(random_date))
    if random_date.isoweekday() == 2:
        print("I dont have vinaigrette")


if __name__ == "__main__":
    print(f"List of files that start with deep: {find_files_with_deep_prefix('images')}")
    print("--------------------------------------\n")

    random_date_between_dates_check_if_monday(input("Enter a date\n"), input("Enter a second date\n"))


