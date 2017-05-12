import os


def make_another_file():
    if os.path.isfile('test.txt'):
        print("You are trying to create a file that already exist!")
    else:
        f = open('test.txt', "w")
        f.write("This is a new text file")


make_another_file()
