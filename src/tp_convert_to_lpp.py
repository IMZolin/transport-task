import numpy as np
from transport_problem import TransportProblem
from linear_programming import LinearProgrammingProblem


def tp_to_lpp(self: TransportProblem):
    """
    transport problem converting
    to cannon linear programming problem
    :self - TransportProblem
    """
    m = self.weight_matrix.shape[0]
    n = self.weight_matrix.shape[1]
    new_lpp_matrix = np.zeros((m * n) * (m + n)).reshape((m + n), (m * n))
    new_b_vector = np.zeros(m + n)
    new_c_vector = np.zeros(m * n)

    lpp = LinearProgrammingProblem()
    lpp.coefficients_matrix = new_lpp_matrix
    lpp.b_vector = new_b_vector
    lpp.c_vector = new_c_vector

    """заполняю условия, соответствующие строкам: sum(...) = a_i"""
    for i in range(m):  # срезы по n элементов заполняются в каждой строке
        for j in range(n):
            lpp.coefficients_matrix[i, j + n*i] = 1
        lpp.b_vector[i] = self.export_a[i]

    """заполняю условия, соответствующие столбцам: sum(...) = b_j (единичные матрицы)"""
    for i in range(n):
        for j in range(m):
            lpp.coefficients_matrix[i + m, i + n*j] = 1
        lpp.b_vector[i + m] = self.import_b[i]

    """заполняю вектор целевой функции"""
    lpp.c_vector = self.weight_matrix.reshape(1, m * n)

    # print(lpp.__dict__)

    return lpp



