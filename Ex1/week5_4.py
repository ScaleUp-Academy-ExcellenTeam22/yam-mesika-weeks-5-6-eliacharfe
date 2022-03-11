import itertools

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
[my_list.append(item) for element in interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))
 for item in itertools.chain(element)]

print(f"Generator version: {my_list}")


# for element in interleave_generator('abc', [1, 2, 3], ('!', '@', '#')):
#     for item in itertools.chain(element):
#         my_list.append(item)

####################################################
####################################################


