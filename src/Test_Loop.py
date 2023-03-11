import numpy as np
from transport_problem import TransportProblem
from tp_convert_to_lpp import tp_to_lpp
from corner_dots import Corner_Dots_Method
from simplex import Simplex_With_Init
from preprocessing import Make_Canon_Form, Update_C


def answer_calculation(self: TransportProblem):
    tp_result = 0
    for i in range(self.basis_solution_matrix.shape[0]):
        for j in range(self.basis_solution_matrix.shape[1]):
            if self.basis_solution_matrix[i][j] is not None:
                tp_result += self.basis_solution_matrix[i][j] * self.weight_matrix[i][j]
    print('\nANSWER:', tp_result)


if __name__ == '__main__':
    weight_matrix_1 = np.array([[2, 6, 5, 3, 0],
                                [3, 2, 1, 4, 0],
                                [3, 6, 2, 5, 0],
                                [3, 6, 5, 6, 0],
                                [3, 6, 5, 7, 0]])

    tp1 = TransportProblem()
    tp1.weight_matrix = weight_matrix_1
    tp1.export_a = np.array([15, 9, 13, 8, 9])
    tp1.import_b = np.array([21, 15, 7, 6, 5])
    tp1.north_west_method()
    tp1.check_optimum()

    while not tp1.is_optimal:
        tp1.loop_calculation()
        tp1.recalculation()
        tp1.check_optimum()
    print(tp1.__dict__)
    answer_calculation(tp1)

    lpp = tp_to_lpp(tp1)
    """making canon form from input data"""
    A2, b2, Ind2 = Make_Canon_Form(lpp.coefficients_matrix.copy(),
                                   lpp.b_vector.copy(),
                                   False,
                                   lpp.coefficients_matrix.shape[1],
                                   0,
                                   0)

    c2, c_free2 = Update_C(A2.copy(), b2.copy(), lpp.c_vector[0].copy(), 0, Ind2, 0, 0, 0)

    """solve the problem using Simplex - Method"""
    Simplex_With_Init(A2.copy(), b2.copy(), Ind2.copy(), c2.copy(), c_free2.copy())
    print('cat')

