def make_text_file():
    a = open('test.txt', "w")
    a.write("This is how you create a new text file.")
    a.close()


def add_some_text():
    a = open('test.txt', "a")
    a.write(" Here is some additional text!")


def even_more_text():
    a = open('test.txt', "a")
    a.write("""
    Here is
    more
    text!!!
    """)


make_text_file()
add_some_text()
even_more_text()
