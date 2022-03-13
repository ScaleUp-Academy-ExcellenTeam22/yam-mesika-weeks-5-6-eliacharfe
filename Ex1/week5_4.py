import itertools
import os
import re
from bs4 import BeautifulSoup

# Mixed Tools

# -- Regular version:


def interleave(*args):
    """
    Take an unlimited list of arguments that can be iterate and returns a list of the elements in order
    for example:
    Input: 'abc', [1, 2, 3], ('!', '@', '#')
    Output: ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
    :param args: An iterable
    :return: A list of elements mixed in order
    """
    list_of_tuples = []
    for elem in zip(*args):
        list_of_tuples.append(elem)
    return list(sum(list_of_tuples, ()))


print(f"Regular version: {interleave('abc', [1, 2, 3], ('!', '@', '#'))}")


#####################################################
# -- Generator version:


def interleave_generator(*args):
    """
    Take an unlimited list of arguments that can be iterate and returns a list of the elements in order
    using generator
    for example:
    Input: 'abc', [1, 2, 3], ('!', '@', '#')
    Output: ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
      :param args: An iterable
    :return: A list of elements mixed in order
    """
    for elem in zip(*args):
        yield elem


my_list = []
my_list += [item for element in interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))
            for item in itertools.chain(element)]

print(f"Generator version: {my_list}")
print("-" * 60)


# for element in interleave_generator('abc', [1, 2, 3], ('!', '@', '#')):
#     for item in itertools.chain(element):
#         my_list.append(item)

####################################################
####################################################
# Harry is rational but not bad


def generate_num_chapter_with_titles(dictionary):
    for filename in os.listdir("resources/potter"):
        file = open("resources/potter/" + filename, "r", encoding="UTF8")
        soup = BeautifulSoup(file, 'html.parser')

        for title in soup.find('title'):
            new_string = title.get_text().replace("Harry Potter and the Methods of Rationality, Chapter", "")
            num_of_chapter = new_string.split()[0][:-1]
            new_file_name = re.sub('[:]', '', new_string)
            dictionary[num_of_chapter] = new_file_name


dictionary = {}
generate_num_chapter_with_titles(dictionary)

for filename_html in os.listdir("resources/potter"):
    for num_chapter, new_filename in dictionary.items():
        if num_chapter == re.sub('[.html]', '', filename_html):
            os.rename("resources/potter/" + filename_html, "resources/potter/" + new_filename + '.html')





            
# def generate_num_chapter_with_titles():
#     for filename in os.listdir("resources/potter"):
#         # try:
#         file = open("resources/potter/" + filename, "r", encoding="UTF8")
#         # except FileNotFoundError:
#         #     print("")
#         soup = BeautifulSoup(file, 'html.parser')
#
#         for title in soup.find('title'):
#             new_string = title.get_text().replace("Harry Potter and the Methods of Rationality, Chapter", "")
#             num_chapter = new_string.split()[0][:-1]
#             new_filename = re.sub('[:]', '', new_string)
#             yield num_chapter, new_filename

        # file.close()


# for num_of_chapter, new_file_name in generate_num_chapter_with_titles():
#     for filename_html in os.listdir("resources/potter"):
#         if num_of_chapter == re.sub('[.html]', '', filename_html):
#             os.rename("resources/potter/" + filename_html, "resources/potter/" + new_file_name)

