from simplex import Simplex_With_Init
from corner_dots import Corner_Dots_Method
import numpy as np
from transport_problem import TransportProblem
from linear_programming import LinearProgrammingProblem
from tp_convert_to_lpp import tp_to_lpp

if __name__ == '__main__':
    weight_matrix = np.array([[14., 28., 21., 28.],
                              [10, 17, 15, 24],
                              [14, 30, 25, 21]])
    export_a = [27.0, 20.0, 43.0]
    import_b = np.array([33.0, 13.0, 27.0, 17.0])

    obj = TransportProblem()
    obj.weight_matrix = weight_matrix
    obj.export_a = export_a
    obj.import_b = import_b

    lpp = tp_to_lpp(obj)
    print(obj.__dict__)

    """solve the problem using corner dots method"""
    Corner_Dots_Method(lpp.c_vector[0].copy(),
                       lpp.b_vector.copy(),
                       lpp.coefficients_matrix.copy(),
                       0)
