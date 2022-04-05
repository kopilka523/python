translate = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
}

user_numders = (input(
    "Введите число от 1 до 10 на английском, которое хотите перевести :"
        )
            )


def numbs_translate (user_numders):
    if user_numders != user_numders.title() or user_numders == user_numders.upper():
        return translate.get(user_numders)
    else:
        user_numders = user_numders.lower()
        return(translate.get(user_numders).capitalize())


print(numbs_translate(user_numders))



