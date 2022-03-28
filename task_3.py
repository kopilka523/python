def get_sign(x):
    if x[0] in '+-':
        return x[0]


arr = ['в',
       '5',
       'часов',
       '17',
       'минут',
       'температура',
       'воздуха',
       'была',
       '+5',
       'градусов'
]
#print(id(arr)) узнаем id списка
i = 0
while i < len(arr):
    sign = get_sign(arr[i])
    if arr[i].isdigit() or (sign and arr[i][1:].isdigit()):
        if sign:
            arr[i] = sign + arr[i][1:].zfill(2)
        else:
            arr[i] = arr[i].zfill(2)

        arr.insert(i, '"')
        arr.insert(i + 2, '"')
        i += 2

    i += 1

#print(arr) проверка данных в списке
#print(id(arr)) проверка что id списка остался прежним
print(" ".join(arr))  # переводим список в строку и выводим

