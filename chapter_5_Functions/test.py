fridge = {'apples': 5, 'oranges': 3, 'milk': 2}
wanted_food = 'apples'


def in_fridge():
    """
    This is a function to see if the fridge has a food.
    """
    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count


print(in_fridge())
print(in_fridge.__doc__)
print(dir())