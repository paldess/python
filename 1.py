class Matrix:
    def __init__(self, str_1):
        self.matrix = str_1
        # print(self.matrix)

    def __str__(self):
        result = str()
        for i in self.matrix:
            for j in i:
                result += str(j)
                result += ' '
            result += '\n'
        return result

    def __add__(self, other):
        try:
            if len(self.matrix) != len(other.matrix):
                return 'матрицы не равны. \nоперация не выполнима'

            result = []
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    return 'матрицы не равны. \nоперация не выполнима'
                res = []
                for j in range(len(self.matrix[i])):
                    x = self.matrix[i][j] + other.matrix[i][j]
                    res.append(x)
                result.append(res)
            result = Matrix(result)
            return result
        except TypeError:
            return  'неслагаемые элементы.\nоперация невыполнима'
mat = Matrix([[1, 3, 1], [2, 2, 2], [3, 3, 3], [9, 9, 9]])
mat2 = Matrix([[4, 4, 4], [5, 5, 5], [6, 6, 6], [9, 9, 9]])
print(mat)
print(mat2)
print(mat2 + mat)

