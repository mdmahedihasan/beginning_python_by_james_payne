__all__ = ['Meal', 'AngryChefException', 'makeBreakfast', 'makeLunch', 'makeDinner', 'Breakfast', 'Lunch', 'Dinner']


def makeBreakfast():
    return Breakfast()


def makeLunch():
    return Lunch()


def makeDinner():
    return Dinner()


class Meal:
    """
    Holds the food and drink used in a meal.
    In true object-oriented tradition, this class
    includes setter methods for the food and drink.
    Call printIt to pretty-print the values.

    """

    def __init__(self, food='omelet', drink='coffee'):
        self.name = 'generic meal'
        self.food = food
        self.drink = drink

    def printIt(self, prefix=''):
        print(prefix, 'A fine', self.name, 'with', self.food, 'and', self.drink)

    def setFood(self, food='omelet'):
        self.food = food

    def setDrink(self, drink='coffee'):
        self.drink = drink

    def setName(self, name=''):
        self.name = name


class Breakfast(Meal):
    def __init__(self):
        Meal.__init__(self, 'omelet', 'coffee')
        self.setName('breakfast')


class Lunch(Meal):
    def __init__(self):
        Meal.__init__(self, 'sandwich', 'gin and tonic')
        self.setName('midday meal')

    def setFood(self, food='sandwich'):
        if food != 'sandwich' and food != 'omelet':
            raise AngryChefException
            Meal.setFood(self, food)


class Dinner(Meal):
    def __init__(self):
        Meal.__init__(self, 'steak', 'merlot')
        self.setName('dinner')

    def printIt(self, prefix=''):
        print(prefix, 'A gourmet', self.name, 'with', self.food, 'and', self.drink)


class SensitiveArtistException(Exception):
    pass


class AngryChefException(Exception):
    pass


def test():
    print("Module test test.")
    print("Testing Meal class")
    m = Meal()
    m.printIt("\t")
    m = Meal('green eggs and ham ', 'tea')
    m.printIt("\t")

    print("Testing Breakfast class")
    b = Breakfast()
    b.printIt("\t")

    b.setName('breaking of the fast')
    b.printIt("\t")

    print("Testing Dinner class")
    d = Dinner()
    d.printIt("\t")

    print("Testing Lunch class")
    l = Lunch()
    l.printIt("\t")

    print("Calling Lunch.setFood()...")
    try:
        l.setFood('hotdog')
    except AngryChefException:
        print("\t", 'The chef is angry. Pick an omelet!')


if __name__ == '__main__':
    test()
