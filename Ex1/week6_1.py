import time


# Fast and Reliable


def build_list_of_words(file):
    """
    Build a list of words from a file given
    :param file: The file containing words
    :return: A list of the words
    """
    return [word for word in file]


def build_set_of_words(file):
    """
    Build a set of words from a file given
    :param file: The file containing words
    :return: A set of the words
    """
    return {word for word in file}


def average_runtime(data_structure, word):
    """
    Gets a data-structure and a word, and search the word a 1000 times while calculating the time that it tooks
    and returns the time
    :param data_structure: The data structure (must be iterable) to search inside
    :param word: A word to search in the data-structure (1000 times)
    :return: The time took to do the mission
    """
    start_time = time.time()
    for i in range(0, 1000):
        if word in data_structure:
            pass
    return time.time() - start_time


long_words_file = open("resources/words.txt")
my_list = build_list_of_words(long_words_file)
my_set = build_set_of_words(long_words_file)

print(f"time of search in list: {average_runtime(my_list, 'zwitterion')}")
print(f"time of search in set: {average_runtime(my_set, 'zwitterion')}")

long_words_file.close()

#############################################
#############################################

