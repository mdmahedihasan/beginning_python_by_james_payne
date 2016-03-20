"""
if type(omelet_type) == type({}):
    print("omelet_type is a dictionary with ingredients")
    return make_food(omelet_type, "omelet")
elif type(omelet_type) == type(""):
    omelet_ingredients = get_omelet_ingredients(omelet_type)
    return make_food(omelet_ingredients, omelet_type)
else:
    raise TypeError("No such omelet type : %s " % omelet_type)
"""
