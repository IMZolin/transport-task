import numpy as np


class TransportProblem:
    def __init__(self):
        self.weight_matrix = np.array([])  # матрица c_i_j
        self.basis_solution_matrix = np.array([])  # матрица, в базисных переменных которой стоят числа
        self.new_basis_variable = np.array([])  # координата новой вводимой переменной
        self.loop_recalculation = np.array([])  # массив координат точек цикла, установленных в определённом порядке
        self.export_a = np.array([])  # a, количество груза в пунктах хранения(a_i в i-ом пункте)
        self.import_b = np.array([])  # b, количество груза в пунктах назначения(b_j в j-ом пункте)
        self.potential_u = np.array([])
        self.potential_v = np.array([])
        self.is_optimal = False
        self.is_closed = True


    def check_optimum(self):
        lenght = len(self.import_b) + len(self.export_a)
        matrix = np.empty([lenght, lenght])
        b_vec = []
        counter = 0
        for i in range(self.basis_solution_matrix.shape[0]):
            for j in range(self.basis_solution_matrix.shape[1]):
                if self.basis_solution_matrix[i][j]!=0:
                    matrix[counter][j]  = 1
                    matrix[counter][i+len(self.import_b)] = -1
                    counter+=1
                    b_vec.append(self.weight_matrix[i][j])
        matrix[counter][len(self.import_b)] = 1
        b_vec.append(0)
        arr = []
        result = np.linalg.solve(matrix, b_vec)
        for i in range(len(self.export_a)):
            for j in range(len(self.import_b)):
                if result[j] - result[len(self.import_b)+i] > self.weight_matrix[i][j]:
                    arr.append(i)
                    arr.append(j)
                    print('Это не оптимальный план')
                    break
        if len(arr) == 0:
            self.is_optimal = True
            print('Опорный план найден')
        else:
            self.new_basis_variable = arr


if __name__ == '__main__':
    weight_matrix = np.array([[14, 28, 21, 28], [10, 17, 15, 24], [14, 30, 25, 21]])
    export_a = [27, 20, 43]
    import_b = np.array([33, 13, 27, 17])
    basis_solution_matrix = np.array([[27, 0, 0, 0], [6, 13, 1,0], [0, 0, 26, 17]])
    obj = TransportProblem()
    obj.weight_matrix = weight_matrix
    obj.export_a = export_a
    obj.import_b = import_b
    obj.basis_solution_matrix = basis_solution_matrix
    TransportProblem.check_optimum(obj)



def __repr__(self):
    return f"TRANSPORT PROBLEM:\nМатрица c_i_j:\n{self.weight_matrix}\nМатрица, в числах которых стоят базисные " \
           f"переменные: \n{self.basis_solution_matrix}\nКоордината новой вводимой переменной: " \
           f"{self.new_basis_variable}\nМассив координат точек цикла, установленных в определённом порядке: " \
           f"{self.loop_recalculation}\nКоличество груза в пунктах хранения: {self.export_a}\nПотенциал u: " \
           f"{self.potential_u}\nПотенциал v: {self.potential_v}\nОптимальность решения: {self.is_optimal}" \
           f"\nЗадача закрыта: {self.is_closed}"