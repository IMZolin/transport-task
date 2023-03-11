import numpy as np
from transport_problem import TransportProblem
from tp_convert_to_lpp import tp_to_lpp
from corner_dots import Corner_Dots_Method
from simplex import Simplex_With_Init
from preprocessing import Make_Canon_Form, Update_C
from prettytable import PrettyTable
from import_adapter import import_data_from_file


if __name__ == '__main__':
    print("\033[0;31;40m\033[0;32;40m\033[0;34;40m")  # COLOR SET

    M, a, b = import_data_from_file()
    tp1 = TransportProblem()
    tp1.weight_matrix = M
    tp1.export_a = a
    tp1.import_b = b

    tp1.execute_potential_method()

    # lpp = tp_to_lpp(tp1)
    # """making canon form from input data"""
    # A2, b2, Ind2 = Make_Canon_Form(lpp.coefficients_matrix.copy(),
    #                                lpp.b_vector.copy(),
    #                                False,
    #                                lpp.coefficients_matrix.shape[1],
    #                                0,
    #                                0)
    #
    # c2, c_free2 = Update_C(A2.copy(), b2.copy(), lpp.c_vector[0].copy(), 0, Ind2, 0, 0, 0)
    #
    # """solve the problem using Simplex - Method"""
    # Simplex_With_Init(A2.copy(), b2.copy(), Ind2.copy(), c2.copy(), c_free2.copy())
    # print('cat')







