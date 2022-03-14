# לחששנית
import re


def find_all_hidden_messages_in_a_binary_file_via_pattern(path, pattern):
    """
    The function gets a path to a binary file, and a binary pattern and search all "strings" that
    matches the pattern (those are coded messages in the file) then returns a list of those messages
    as regular strings.
    :return: A list of the hidden messages
    """
    with open(path, "rb") as encrypted_binary_file:
        list_hidden_messages = []
        for line in encrypted_binary_file.readlines():
            hidden_messages = re.compile(pattern).findall(line)
            if hidden_messages:
                list_hidden_messages += [hidden_msg.decode('ascii') for hidden_msg in hidden_messages]
        return list_hidden_messages


if __name__ == '__main__':
    print('\n'.join(
        find_all_hidden_messages_in_a_binary_file_via_pattern("resources/logo.jpg", b'[a-z]{5,}!')))

