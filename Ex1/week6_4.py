from PIL import Image


def decoding_message_in_image(path):
    """
    In each column of the image there is a pixel painted black.
    The pixel is colored by the line number that corresponds to the numeric value of the character.
    If you convert the position where the black pixels are in order, from left to right, you get the
    hidden message.
    :param path: The path to an image
    :return: The hidden message
    """
    img = Image.open(path)
    pixels = img.load()
    width = img.size[0]
    height = img.size[1]
    return ''.join([chr(row) for col in range(width) for row in range(height) if pixels[col, row] == 1])


if __name__ == '__main__':
    print(decoding_message_in_image("resources/code.png"))
    # Returns: "Place gunpowder beneath the House of Lords. 11/05/1605"

