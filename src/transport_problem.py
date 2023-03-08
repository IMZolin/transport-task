import numpy as np


class TransportProblem:
    def __init__(self):
        self.weight_matrix = np.array([])  # матрица c_i_j
        self._basis_solution_matrix = np.array([])  # матрица, в базисных переменных которой стоят числа
        self._new_basis_variable = np.array([])  # координата новой вводимой переменной
        self._loop_recalculation = np.array([])  # массив координат точек цикла, установленных в определённом порядке
        self._export_a = np.array([])  # a, количество груза в пунктах хранения(a_i в i-ом пункте)
        self._import_b = np.array([])  # b, количество груза в пунктах назначения(b_j в j-ом пункте)
        self._potential_u = np.array([])
        self._potential_v = np.array([])
        self._is_optimal = False
        self._is_closed = True

    def __repr__(self):
        return f"TRANSPORT PROBLEM:\nМатрица c_i_j:\n{self.weight_matrix}\nМатрица, в числах которых стоят базисные " \
               f"переменные: \n{self._basis_solution_matrix}\nКоордината новой вводимой переменной: " \
               f"{self._new_basis_variable}\nМассив координат точек цикла, установленных в определённом порядке: " \
               f"{self._loop_recalculation}\nКоличество груза в пунктах хранения: {self._export_a}\nПотенциал u: " \
               f"{self._potential_u}\nПотенциал v: {self._potential_v}\nОптимальность решения: {self._is_optimal}" \
               f"\nЗадача закрыта: {self._is_closed}"
