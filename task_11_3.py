class MyOwnErr(Exception):
    pass


class UserInput(MyOwnErr):
    input_list = []

    @staticmethod
    def check_list():
        number = None

        while number != "Stop":
            try:
                number = input('Введите число или "Stop" для выхода и просмотра результата: ')
                if not number.isdigit():
                    if number != "Stop":
                        raise MyOwnErr
            except MyOwnErr:
                print('Нужно ввести число или "Stop"')
                continue
            else:
                if number == "Stop":
                    return f'Список введенных чисел:\n{UserInput.input_list}'
                UserInput.input_list.append(int(number))
                continue


res = UserInput.check_list()
print(res)
