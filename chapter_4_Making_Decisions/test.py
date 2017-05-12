omelet_ingredients = {"egg": 2, "mushroom": 5, "pepper": 1, "cheese": 1, "milk": 1}
fridge_contents = {"egg": 10, "mushroom": 20, "pepper": 3, "cheese": 2, "tomato": 4, "milk": 15}
have_ingredients = [False]

if fridge_contents["egg"] > omelet_ingredients["egg"]:
    have_ingredients[0] = True
have_ingredients.append("egg")
print(have_ingredients)

if fridge_contents["mushroom"] > omelet_ingredients["mushroom"]:
    if have_ingredients[0] == False:
        have_ingredients[0] = True
    have_ingredients.append("mushroom")
print(have_ingredients)

if fridge_contents["pepper"] > omelet_ingredients["pepper"]:
    if have_ingredients[0] == True:
        have_ingredients[0] = False
    have_ingredients.append("pepper")

if fridge_contents["cheese"] > omelet_ingredients["cheese"]:
    if have_ingredients[0] == False:
        have_ingredients[0] = True
    have_ingredients.append("cheese")

if fridge_contents["milk"] > omelet_ingredients["milk"]:
    if have_ingredients[0] == True:
        have_ingredients[0] = False
    have_ingredients.append("milk")

if have_ingredients[0] == True:
    print("I have the ingredients to make an omelet!")
