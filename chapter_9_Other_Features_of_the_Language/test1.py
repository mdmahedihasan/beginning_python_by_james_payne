filter_me = [1, 2, 3, 4, 6, 7, 8, 11, 12, 14, 15, 19, 22]
func = lambda x: x % 2 == 0
result = filter(func, filter_me)
print(result)
