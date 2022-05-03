class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return ComplexNumber(self.number + other.number)

    def __mul__(self, other):
        return ComplexNumber(self.number * other.number)

    def __str__(self):
        return f'{self.number}'


n_1 = ComplexNumber(complex(' 1+2j '))
n_2 = ComplexNumber(complex(' 2-3j '))
n_3 = ComplexNumber(complex('   0.1+2.0j'))
print(f'Сложение: {n_1 + n_2 + n_3}')
print(f'Умножение: {n_1 * n_2 * n_3}')
