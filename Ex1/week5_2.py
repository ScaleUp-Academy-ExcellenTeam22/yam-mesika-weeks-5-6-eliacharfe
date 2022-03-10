# Cup of join


def join(*args, sep='-'):
    """
    The function a unlimited number a lists and an option parameter (called sep) and put it between each 2 lists,
    if nothing is passed in the parameter will put by default the character '-'
    :param args: lists of arguments
    :param sep: the parameter to put between each 2 lists
    :return: a new list with the elements of the lists which between the elements of 2 different lists there
    is sep (or '-' by default)
    """
    if not args:
        return None
    lst = []
    for lst_args in args:
        [lst.append(argument) for argument in lst_args]
        lst.append(sep)
    return lst[:-1]


print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())


print("-----------------------------------------")
###################################################
###################################################
# Piece of cake


def get_recipe_price(prices, optionals=[], **ingredients):
    """
    This function calculates how much we need to pay for the ingredients passed (with their price and quantity
     for 100g) in order to form a recipe
    :param prices: A dictionary of ingredients with their prices (the values are their price for 100g)
    :param optionals: An optional parameter that gets a list of ingredients to ignore
    :param ingredients: In each argument passed in the parameter we specify the name of the ingredient and its value
    is the amount (in grams) that we need to buy for the recipe
    :return: The price we need to pay for buying the indgredients to the recipe
    """
    sum = 0
    for key in prices:
        for ingredient in ingredients:
            if key == ingredient and not ingredient in optionals:
                sum += prices[key] * ingredients.get(key) // 100
    return sum


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))

#######################################################
