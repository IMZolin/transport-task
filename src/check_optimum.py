from numpy import np


def check_optimum(self):
    lenght = len(self.import_b) + len(self.export_a)
    matrix = np.zeros([lenght, lenght], dtype=int)
    b_vec = []
    counter = 0
    for i in range(self.basis_solution_matrix.shape[0]):
        for j in range(self.basis_solution_matrix.shape[1]):
            if self.basis_solution_matrix[i][j] != None:
                matrix[counter][j] = 1
                matrix[counter][i + len(self.import_b)] = -1
                counter += 1
                b_vec.append(self.weight_matrix[i][j])
    matrix[counter][len(self.import_b)] = 1
    b_vec.append(0)
    arr = []
    result = np.linalg.solve(matrix, b_vec)
    for i in range(len(self.export_a)):
        for j in range(len(self.import_b)):
            if result[j] - result[len(self.import_b) + i] > self.weight_matrix[i][j]:
                arr.append(i)
                arr.append(j)
                print('Это не оптимальный план')
                break
    if len(arr) == 0:
        self.is_optimal = True
        print('Опорный план найден')
    else:
        self.new_basis_variable = arr