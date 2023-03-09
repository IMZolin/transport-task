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

    print(lpp.__dict__)

    return lpp


if __name__ == '__main__':
    weight_matrix = np.array([[14, 28, 21, 28],
                              [10, 17, 15, 24],
                              [14, 30, 25, 21]])
    export_a = [27, 20, 43]
    import_b = np.array([33, 13, 27, 17])

    obj = TransportProblem()
    obj.weight_matrix = weight_matrix
    obj.export_a = export_a
    obj.import_b = import_b

    tp_to_lpp(obj)
    print(obj.__dict__)



