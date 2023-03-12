from transport_problem import TransportProblem
from import_adapter import import_data_from_file


if __name__ == '__main__':
    print("\033[0;31;40m\033[0;32;40m\033[0;34;40m")  # COLOR SET

    M, a, b = import_data_from_file()
    tp1 = TransportProblem()
    tp1.weight_matrix = M
    tp1.export_a = a
    tp1.import_b = b

    tp1.execute_potential_method()








