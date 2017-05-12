fridge_contents = {"egg": 8, "mushroom": 20, "pepper": 3, "cheese": 12, "tomato": 5, "milk": 13}

try:
    if fridge_contents["orange juice"] > 3:
        print("Let's have some juice")
except(KeyError) as error:
    print("Aww, there is no %s" % error)
except(TypeError):
    pass
