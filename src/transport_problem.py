import numpy as np
from check_optimum import check_optimum


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


    check_optimum = check_optimum

if __name__ == '__main__':

    weight_matrix = np.array([[14, 28, 21, 28],
                              [10, 17, 15, 24],
                              [14, 30, 25, 21]])
    export_a = [27, 20, 43]
    import_b = np.array([33, 13, 27, 17])
    basis_solution_matrix = np.array([[27, None, None, None],
                                      [6, 13, 1, None],
                                      [None, None, 26, 17]])
    obj = TransportProblem()
    obj.weight_matrix = weight_matrix
    obj.export_a = export_a
    obj.import_b = import_b
    obj.basis_solution_matrix = basis_solution_matrix

    check_optimum(obj)
    print(obj.__dict__)

def __repr__(self):
    return f"TRANSPORT PROBLEM:\nМатрица c_i_j:\n{self.weight_matrix}\nМатрица, в числах которых стоят базисные " \
           f"переменные: \n{self.basis_solution_matrix}\nКоордината новой вводимой переменной: " \
           f"{self.new_basis_variable}\nМассив координат точек цикла, установленных в определённом порядке: " \
           f"{self.loop_recalculation}\nКоличество груза в пунктах хранения: {self.export_a}\nПотенциал u: " \
           f"{self.potential_u}\nПотенциал v: {self.potential_v}\nОптимальность решения: {self.is_optimal}" \
           f"\nЗадача закрыта: {self.is_closed}"