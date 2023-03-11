
def recalculation(self):
    '''
    Процедура пересчета матрицы базисных переменных.
    Расставляем знаки, берём минимум и производим сложение или вычитание, в соответствии со знаком.
    В функции вместо знаков используется характеристика целых чисел, опредедяющая способность числа делиться на 2 (чётность/нечётность)
    "отрицательными" ячейками оказываются чётные, положительными - нечётные. Это обусловлено тем, что в первой точке цикла может стоять None
    (а вот всегда ли он там будет, и можно ли просто брать срез, завтра надо подумать)
    '''
    arr = self.loop_recalculation[1::]
    matrix = self.basis_solution_matrix
    #arr_odd_val - массив из элементов матрицы базисных элементов, стоящих на чётных позициях в цикле пересчёта (я знаю про путаницу с обозначениями, завтра подумаю)
    arr_odd_val = []
    #массивы чётных и нечётных (по индексам) точек цикла пересчёта
    arr_even = []
    arr_odd = []
    #arr - массив массивов из точек цикла
    for i in range(len(arr)):
        if i%2!=0:
            arr_even.append(arr[i])
        else:
            arr_odd.append(arr[i])
    for sub_arr in arr_odd:
        arr_odd_val.append(matrix[sub_arr[0],sub_arr[1]])
    delta = min(arr_odd_val)
    for sub_arr in arr_odd:
        matrix[sub_arr[0],sub_arr[1]] -= delta
    for sub_arr in arr_even:
        matrix[sub_arr[0], sub_arr[1]] += delta
    self.basis_solution_matrix = matrix