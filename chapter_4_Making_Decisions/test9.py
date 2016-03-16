for food in ("pate", "cheese", "rotten apples", "crackers", "whip cream", "tomato soup"):
    if food[0:6] == "rotten":
        continue
    print("Hey you can eat %s" % food)
