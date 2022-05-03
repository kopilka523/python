class MyOwnErr(Exception):
    pass


class Division(MyOwnErr):

    @staticmethod
    def number_check(number_1, number_2):
        try:
            if number_2 == 0:
                raise MyOwnErr
        except MyOwnErr:
            print('Делитель не может быть нулем')
            number_2 = int(input('Введите делитель: '))
            return Division.number_check(number_1, number_2)
        else:
            return f'Результат: {number_1 / number_2}'


print(Division.number_check(number_1=int(input('Введите делимое: ')), number_2=int(input('Введите делитель: '))))
