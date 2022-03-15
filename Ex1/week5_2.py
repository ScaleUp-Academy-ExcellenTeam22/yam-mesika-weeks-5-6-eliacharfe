# Cup of join


def join(*args, sep='-'):
    """
    The function a unlimited number a lists and an option parameter (called sep) and put it between each
    2 lists, if nothing is passed in the parameter will put by default the character '-'.
    :param args: Lists of arguments.
    :param sep: The parameter to put between each 2 lists.
    :return: A new list with the elements of the lists which between the elements of 2 different
    lists there is sep (or '-' by default).
    """
    if not args:
        return None
    lst = []
    for lst_args in args:
        lst += [argument for argument in lst_args]
        lst.append(sep)
    return lst[:-1]


# Piece of cake


def get_recipe_price(prices, optionals=[], **ingredients):
    """
    This function calculates how much we need to pay for the ingredients passed (with their price
    and quantity for 100g) in order to form a recipe.
    :param prices: A dictionary of ingredients with their prices (the values are their price for 100g).
    :param optionals: An optional parameter that gets a list of ingredients to ignore.
    :param ingredients: In each argument passed in the parameter we specify the name of the ingredient
    and its value is the amount (in grams) that we need to buy for the recipe.
    """
    price_of_ingredients = 0
    for key in prices:
        for ingredient in ingredients:
            if key == ingredient and ingredient not in optionals:
                price_of_ingredients += prices[key] * ingredients.get(key) // 100
    return price_of_ingredients


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
    print("-----------------------------------------")

    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))

