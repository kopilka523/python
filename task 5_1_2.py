from itertools import islice

odd_to_15 = (i for i in range(1, 15 + 1, 2))
print(type(odd_to_15))
print(*islice(odd_to_15, 8))