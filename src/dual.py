from preprocessing import Make_Canon_Form, Update_C
from corner_dots import Corner_Dots_Method
from simplex import Simplex_With_Init
from transport_problem import TransportProblem
from tp_convert_to_lpp import tp_to_lpp
from import_adapter import import_data_from_file


def parse_to_dual(A, b_, c_, Less_, More_, var_positive_amount):
    """solve min task only"""

    """change all <= to >="""
    for i in range(Less_):
        A[i, :] = -A[i, :]
        b_[i] = -b_[i]

    c_dual_ = b_
    """max -> min"""
    c_dual_[:] = -c_dual_[:]

    b_dual_ = c_
    A_dual_ = A.T
    A_dual_ = A_dual_.astype(float)

    X_Positive_dual_ = Less_ + More_
    Less_dual = var_positive_amount
    More_dual = 0

    return A_dual_, b_dual_, c_dual_, X_Positive_dual_, Less_dual, More_dual, X_Positive_dual_


if __name__ == "__main__":

    M, a, b = import_data_from_file()
    tp1 = TransportProblem()
    tp1.weight_matrix = M
    tp1.export_a = a
    tp1.import_b = b

    tp1.to_close()

    lpp = tp_to_lpp(tp1)

    """Адаптированный под транспортную задачу вариант: Less and More принимают нулевые значения. Это только здесь
     и только  потому, что в задаче изначально даются только равенства. А так вообще надо подставлять нормально"""
    A_dual, b_dual, c_dual, X_Positive_dual, Less, More, X_Positive_dual = parse_to_dual(lpp.coefficients_matrix,
                                                                                         lpp.b_vector,
                                                                                         lpp.c_vector,
                                                                                         0,
                                                                                         0,
                                                                                         lpp.coefficients_matrix.shape[1])
    """make canon form from dual"""
    A_dual, b_dual, Ind_dual = Make_Canon_Form(A_dual.copy(),
                                               b_dual[0].copy(),
                                               False,
                                               X_Positive_dual,
                                               Less,
                                               More)

    c_dual, c_free_dual = Update_C(A_dual.copy(),
                                   b_dual.copy(),
                                   c_dual.copy(),
                                   0,
                                   Ind_dual.copy(),
                                   Less,
                                   More,
                                   lpp.coefficients_matrix.shape[0] - X_Positive_dual)

    """solve with Simplex Method"""
    Simplex_With_Init(A_dual.copy(),
                      b_dual.copy(),
                      Ind_dual.copy(),
                      c_dual.copy(),
                      c_free_dual.copy())

    """solve with Corner Dots Method"""
    Corner_Dots_Method(c_dual, b_dual.copy(), A_dual, c_free_dual)
