import numpy as np
from loop_recalculation_file import loop_calculation
from check_optimum import check_optimum
from north_west_method import north_west_method


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
    north_west_method = north_west_method
    loop_calculation = loop_calculation
    
    def __repr__(self):
        return f"TRANSPORT PROBLEM:\nМатрица c_i_j:\n{self.weight_matrix}\nМатрица, в числах которых стоят базисные " \
               f"переменные: \n{self.basis_solution_matrix}\nКоордината новой вводимой переменной: " \
               f"{self.new_basis_variable}\nМассив координат точек цикла, установленных в определённом порядке: " \
               f"{self.loop_recalculation}\nКоличество груза в пунктах хранения: {self.export_a}\nПотенциал u: " \
               f"{self.potential_u}\nПотенциал v: {self.potential_v}\nОптимальность решения: {self.is_optimal}" \
               f"\nЗадача закрыта: {self.is_closed}"

    


