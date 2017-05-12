fridge_contents = {"egg": 3, "Mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 5, "milk": 13}

try:
    if fridge_contents["orange juice"] > 3:
        print("Let's have some juice")
except (KeyError, TypeError) as error:
    print("Aww, there is no %s" % error)
