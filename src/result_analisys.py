import numpy as np
from transport_problem import TransportProblem
from prettytable import PrettyTable
from preprocessing import Make_Canon_Form, Update_C
from linear_programming import  LinearProgrammingProblem
from simplex import Simplex_With_Init
from tp_convert_to_lpp import tp_to_lpp


def generate_problem(n, m):
    matrix = np.random.randint(50, size=(n, m))
    a = np.random.randint(50, size=n)
    b = np.random.randint(50, size=m)
    sum_a = a.sum()
    sum_b = b.sum()
    #  делаем условие закрытым
    if sum_a < sum_b:
        a[-1] = sum_b - (sum_a - a[-1])
    elif sum_a > sum_b:
        b[-1] = sum_a - (sum_b - b[-1])
    return matrix, a, b


def Simplex_Time_Recorder(self: LinearProgrammingProblem):
    A2, b2, Ind2 = Make_Canon_Form(self.coefficients_matrix.copy(),
                                   self.b_vector.copy(),
                                   False,
                                   self.coefficients_matrix.shape[1],
                                   0,
                                   0)

    c2, c_free2 = Update_C(A2.copy(), b2.copy(), self.c_vector[0].copy(), 0, Ind2, 0, 0, 0)

    """solve the problem using Simplex - Method"""
    Simplex_With_Init(A2.copy(), b2.copy(), Ind2.copy(), c2.copy(), c_free2.copy())


def Potentials_Time_Recorder(self: TransportProblem):
    self.north_west_method()
    self.check_optimum()

    while not self.is_optimal:
        self.loop_calculation()
        # self.steps_visualisation()
        self.recalculation()
        self.check_optimum()

    table = PrettyTable()
    table.header = False
    table.add_rows(self.basis_solution_matrix)
    self.answer_calculation()
    print('Итоговая матрица базисных элементов:')
    print(table)



if __name__ == '__main__':
    print("\033[0;31;40m\033[0;32;40m\033[0;34;40m")  # COLOR SET

    M, a, b = generate_problem(5, 7)
    tp1 = TransportProblem()


    # M = np.array([[8, 9, 11, 32, 24, 24, 0],
    #               [32, 23, 25, 7, 17, 20, 8],
    #               [16, 9, 26, 27, 35, 36, 45],
    #               [20, 48, 26, 6, 31, 30, 45],
    #               [0, 4, 13, 42, 10, 49, 21]])
    # a = np.array([43, 42, 30, 14, 24])
    # b = np.array([5, 2, 42, 17, 24, 26, 37])

    tp1.weight_matrix = M
    tp1.export_a = a
    tp1.import_b = b

    Potentials_Time_Recorder(tp1)

    lpp = tp_to_lpp(tp1)

    Simplex_Time_Recorder(lpp)

    print('cat')