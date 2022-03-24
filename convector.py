#1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах

duration = int(input("Введите количество секунд : "))

day = duration // 86400
hour = (duration-(day*86400))//3600
minute = (duration - ((day*86400) + (hour*3600)))//60
second = duration - ((day*86400) + (hour*3600) + (minute*60))

if 60 > duration > 0:
    print(duration, " -секунд")
elif 60 <= duration < 3600:
    print(minute, " -минут", second, " -секунд")
elif 3600 <= duration < 86400:
    print(hour, "-часов", minute, " -минут", second, " -секунд")
elif duration >= 86400:
    print(day, "-дней", hour, "-часов", minute, " -минут", second, " -секунд")
else:
    print("Введите число больше 0")