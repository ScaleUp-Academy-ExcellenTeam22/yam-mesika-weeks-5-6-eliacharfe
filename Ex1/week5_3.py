# לחששנית
import re


def find_all_hidden_messages_in_a_binary_file_via_pattern(path, pattern):
    """
    The function gets a path to a binary file, and a binary pattern and search all "strings" that
    matches the pattern (those are coded messages in the file) then returns a list of those messages
    as regular strings.
    :return: A list of the hidden messages
    """
    reg = re.compile(pattern)
    with open(path, "rb") as encrypted_binary_file:
        list_hidden_messages = []
        list_hidden_messages += [hidden_msg.decode('ascii') for line in encrypted_binary_file.readlines()
                                 if reg.findall(line) for hidden_msg in reg.findall(line)]
        return list_hidden_messages


if __name__ == '__main__':
    print('\n'.join(
        find_all_hidden_messages_in_a_binary_file_via_pattern("resources/logo.jpg", b'[a-z]{5,}!')))






    # with open(path, "rb") as encrypted_bin_file:
    #     list_hidden_messages = []
    #     for line in encrypted_binary_file.readlines():
    #         if re.compile(pattern).findall(line):
    #             lst_hidden_messages += [hidden_msg.decode('ascii') for hidden_msg in re.compile(pattern).findall(line)]
    #     return lst_hidden_messages
