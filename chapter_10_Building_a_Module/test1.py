import test

print("Making a breakfast")
breakfast = test.makeBreakfast()

breakfast.printIt('\t')

print("Making a lunch")
lunch = test.makeLunch()

try:
    lunch.setFood('pancakes')
except test.AngryChefException:
    print('\t', "Can not make a lunch of pancakes")
    print('\t', 'The chef is angry. Pick an omelet')
