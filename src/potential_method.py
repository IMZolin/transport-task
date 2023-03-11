from prettytable import PrettyTable


def execute_potential_method(self):
    self.north_west_method()
    self.check_optimum()

    while not self.is_optimal:
        self.loop_calculation()
        self.steps_visualisation()
        self.recalculation()
        self.check_optimum()

    table = PrettyTable()
    table.header = False
    table.add_rows(self.basis_solution_matrix)
    self.answer_calculation()
    print('Итоговая матрица базисных элементов:')
    print(table)
