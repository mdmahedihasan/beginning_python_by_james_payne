def print_line_lengths():
    a = open("test.txt", "r")
    text = a.readlines()
    for line in text:
        print(len(line))


print_line_lengths()
