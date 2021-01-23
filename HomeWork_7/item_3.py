#Класс Органическая клетка

class OrganicCell:
    def __init__(self, count_cell: int):
        self.count_cell = count_cell

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return OrganicCell(self.count_cell + other.count_cell)
        else:
            TypeError

    def __sub__(self, other):
        sub_cells = self.count_cell - other.count_cell
        if sub_cells > 0:
            return OrganicCell(sub_cells)
        else:
            print (ValueError('Разность количества ячеек двух клеток <= 0. Операция невозможна.'))

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return OrganicCell(self.count_cell * other.count_cell)
        else:
            TypeError

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return OrganicCell(self.count_cell // other.count_cell)
        else:
            TypeError

    def make_order(self, count_cell_in_row):
        result_str = ''
        list_cell = []
        row_cells = '*' * self.count_cell
        for i in range(0, len(row_cells), count_cell_in_row):
            list_cell.append(row_cells[i:i + count_cell_in_row])
        result_str = "\\n".join(list_cell)
        return result_str

cell_001 = OrganicCell(12)
cell_002 = OrganicCell(4)
cell_003 = OrganicCell(20)
cell_004 = OrganicCell(7)

print(cell_001.make_order(5))
print(cell_002.make_order(5))
print(cell_003.make_order(5))

cell_add = cell_001 + cell_002
print(f"Кол-во ячеек cell_add = {cell_add.count_cell}; ячейки по рядам: {cell_add.make_order(5)}")

cell_sub = cell_002 - cell_001
if not (cell_sub is None):
    print(f"Кол-во ячеек cell_sub = {cell_sub.count_cell}; ячейки по рядам: {cell_sub.make_order(5)}")

cell_mul = cell_002 * cell_004
print(f"Кол-во ячеек cell_mul = {cell_mul.count_cell}; ячейки по рядам: {cell_mul.make_order(5)}")

cell_div = cell_003 / cell_004
print(f"Кол-во ячеек cell_div = {cell_div.count_cell}; ячейки по рядам: {cell_div.make_order(5)}")

