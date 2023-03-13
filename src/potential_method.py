from prettytable import PrettyTable


def execute_potential_method(self):
    table0 = PrettyTable()
    table0.header = False
    table0.add_rows(self.weight_matrix)
    print('До проверки на закрытость:')
    print('Объем груза, хранящийся у поставщиков:')
    print(self.export_a)
    print('Объем груза, который необходимо доставить каждому из производителей:')
    print(self.import_b)
    print('Весовая матрица:')
    print(table0)


    self.to_close()

    table0 = PrettyTable()
    table0.header = False
    table0.add_rows(self.weight_matrix)
    print('\nПосле проверки на закрытость:')
    print('Объем груза, хранящийся у поставщиков:')
    print(self.export_a)
    print('Объем груза, который необходимо доставить каждому из производителей:')
    print(self.import_b)
    print('Весовая матрица:')
    print(table0)

    print('\n\n')


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
