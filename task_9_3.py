class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Position - {self.position}: {sum(self._income.values())} $'


p = Position('Сергей', 'Щербина', 'junior', 600, 300)
print(p.get_full_name())
print(p.get_total_income())
