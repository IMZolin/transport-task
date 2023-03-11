import numpy as np
from transport_problem import TransportProblem
from tp_convert_to_lpp import tp_to_lpp
from corner_dots import Corner_Dots_Method


if __name__ == '__main__':
    weight_matrix_1 = np.array([[2, 6, 5, 3, 0],
                                [3, 2, 1, 4, 0],
                                [3, 6, 2, 5, 0],
                                [3, 6, 5, 6, 0],
                                [3, 6, 5, 7, 0]])
    # matrix1 = np.array([[15, None, None, None, None],
    #                     [None, 2, 7, None, None],
    #                     [6, 1, None, 6, None],
    #                     [None, 8, None, None, None],
    #                     [None, 4, None, None, 5]])

    tp1 = TransportProblem()
    tp1.weight_matrix = weight_matrix_1
    tp1.export_a = np.array([21, 3, 13, 8, 9])
    tp1.import_b = np.array([21, 15, 7, 6, 5])
    # tp1.basis_solution_matrix = matrix1
    tp1.north_west_method()
    tp1.check_optimum()
    while not tp1.is_optimal:
        tp1.loop_calculation()
        tp1.recalculation()
        tp1.check_optimum()
    print(tp1.__dict__)

    # lpp = tp_to_lpp(tp1)
    #
    # """solve the problem using corner dots method"""
    # Corner_Dots_Method(lpp.c_vector[0].copy(),
    #                    lpp.b_vector.copy(),
    #                    lpp.coefficients_matrix.copy(),
    #                    0)




