src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
for i in range(1, len(src)):
    if int(src[i]) > int(src[i - 1]):
        print(src[i])