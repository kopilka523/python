class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        return Matrix([[self.matrix_list[0][0] + other.matrix_list[0][0],
                        self.matrix_list[0][1] + other.matrix_list[0][1]],
                       [self.matrix_list[1][0] + other.matrix_list[1][0],
                        self.matrix_list[1][1] + other.matrix_list[1][1]]])

    def __str__(self):
        return f'[{self.matrix_list[0]}\n {self.matrix_list[1]}]'


matrix_1 = Matrix([[4, -2], [5, 8]])
matrix_2 = Matrix([[9, -1], [6, 4]])

print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 + matrix_2)
