# Group by


def group_by(func, iterable):
    """
    Gets a function and an iterable and returns a dictionary which the keys are what the function
    returns on the item of the iterable and the value is a list of the items that the result
    on those items it is this key.
    Possible input:   len, ["hi", "bye", "yo", "try"]
    Output:           {2: ["hi", "yo"], 3: ["bye", "try"]}
    :param func: A function
    :param iterable: An iterable
    :return: Dictionary of key and value like explained
    """
    dic = {}
    for item in iterable:
        if func(item) in dic:
            dic[func(item)].append(item)
        else:
            dic[func(item)] = [item]
    return dic


print(group_by(len, ["hi", "bye", "yo", "try"]))
print("------------------------------------------")
#################################################
# zipwith


def zip_with(func, *args):
    """
    Gets a function (func) and an unlimited number of iterables with the same length, and activate the
    function on all the items of the iterable that are on same place in order.
    Input (possible):  sum, [1, 2, 3], [4, 5, 6]
    Output:            [5, 7, 9]
    :param func: A function
    :param args: A list of iterables with the same length
    :return: List of the results that the function passed returns on each item of the iterables in order
    """
    return [func(item) for item in zip(*args)]


print(zip_with(sum, [1, 2, 3], [4, 5, 6]))
print(zip_with(max, (5, 4), (2, 5), (6, -6)))
print(zip_with(max, (5, 4), (2, 5), (6, -6), (11, 9)))

print("-------------------------------------------")
###################################################
