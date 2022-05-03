class Cell:
    def __init__(self, cell_of_the_cell):
        self.cell_of_the_cell = cell_of_the_cell

    def __add__(self, other):
        return Cell(self.cell_of_the_cell + other.cell_of_the_cell)

    def __sub__(self, other):
        difference = self.cell_of_the_cell - other.cell_of_the_cell
        return Cell(difference) if difference > 0 else f'Разница отрицательная'

    def __mul__(self, other):
        return Cell(self.cell_of_the_cell * other.cell_of_the_cell)

    def __floordiv__(self, other):
        return Cell(self.cell_of_the_cell // other.cell_of_the_cell)

    def make_order(self):
        row = '***** \\n ' * (self.cell_of_the_cell // 5)
        rest = '*' * (self.cell_of_the_cell % 5)
        return f'{row}{rest}'

    def __str__(self):
        return f'{self.cell_of_the_cell}\n{Cell.make_order(self)}'


cell_1 = Cell(8)
cell_2 = Cell(3)
print(f'Объединение: {cell_1 + cell_2}')
print(f'Вычитание: {cell_1 - cell_2}')
print(f'Умножение: {cell_1 * cell_2}')
print(f'Деление: {cell_1 // cell_2}')

