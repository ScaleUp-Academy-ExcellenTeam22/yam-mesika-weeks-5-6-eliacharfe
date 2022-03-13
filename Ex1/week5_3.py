# לחששנית


def whisperer():
    """
    Open a binary file with encrypted messages in a logo, the messages are words that have only
    lowercase letters more or equals to 5 length that ends by the character '!'. The function
    returns a list of those messages
    :return: A list of the hidden messages
    """
    with open("resources/logo.jpg", "rb") as file:
        counter = 0
        lst = []
        word = ''

        for line in file.readlines():
            for char in line:
                if char in range(97, 123):
                    counter += 1
                    word += chr(char)
                if counter >= 5 and char == 33:
                    lst.append(word + chr(char))
                    counter = 0
                    word = ''
                if char not in range(97, 123):
                    counter = 0
                    word = ''
        return lst


print(whisperer())