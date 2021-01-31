# Склад оргтехники
from abc import ABC, abstractmethod
import datetime
from collections import defaultdict

# Оргтехника
class Technics(ABC):

    _dict_technics = {
                       'Printer': 0,
                       'Scaner': 0,
                       'Xserox': 0
                     }

    def __init__(self, type_technic, serial_number, producer, model, price):
        self.type_technic  = type_technic   # тип техники
        self.serial_number = serial_number  # серийный номер
        self.producer      = producer       # производитель
        self.model         = model          # модель
        self.price         = price          # цена

    @abstractmethod
    def take_in(self, total):
        pass

    @abstractmethod
    def take_out(self, total):
        pass

    @classmethod
    def get_rests(self):
        for key, value in Technics._dict_technics.items():
            print(f"Вид техники: {key}; Кол-во = {value}")

class Printer(Technics):
    def __init__(self, type_technic, serial_number, producer, model, price,
                       speed_print, colors: bool, printer_type
                 ):
        super().__init__(type_technic, serial_number, producer, model, price)
        self.speed_print  = speed_print  # скорость печати
        self.colors       = colors       # цветной / ЦБ
        self.printer_type = printer_type # тип принтера (лазерный, струйный, матричный)

    @classmethod
    def take_in(self, total):
        Technics._dict_technics[self.__name__] += total

    @classmethod
    def take_out(self, total):
        total_now = Technics._dict_technics[self.__name__]
        if total_now >= total:
            Technics._dict_technics[self.__name__] -= total
        else:
            err = f"Недопустимое кол-во {self.__name__} для списания"
            raise ValueError(err)

class Scaner(Technics):
    def __init__(self, type_technic, serial_number, producer, model, price,
                 kind, speed_scaner, resolution):
        super().__init__(type_technic, serial_number, producer, model, price)
        self.kind         = kind         # вид (планшетный, барабанный, 3D)
        self.speed_scaner = speed_scaner # скорость сканирования
        self.resolution   = resolution   # разрешение (dpi)

    @classmethod
    def take_in(self, total):
        Technics._dict_technics[self.__name__] += total

    @classmethod
    def take_out(self, total):
        total_now = Technics._dict_technics[self.__name__]
        if total_now >= total:
            Technics._dict_technics[self.__name__] -= total
        else:
            err = f"Недопустимое кол-во {self.__name__} для списания"
            raise ValueError(err)

class Xserox(Technics):
    def __init__(self, type_technic, serial_number, producer, model, price,
                 duplex: bool, format):
        super().__init__(type_technic, serial_number, producer, model, price)
        self.duplex = duplex         # 2-сторонняя печать
        self.format = format # формат (А4, А2)

    @classmethod
    def take_in(self, total):
        Technics._dict_technics[self.__name__] += total

    @classmethod
    def take_out(self, total):
        total_now = Technics._dict_technics[self.__name__]
        if total_now >= total:
            Technics._dict_technics[self.__name__] -= total
        else:
            err = f"Недопустимое кол-во {self.__name__} для списания"
            raise ValueError(err)

#Склад
class StoreTechnics:
    dict_cells = {
                   'Printer:Laser': 'A-1',
                   'Printer:HP': 'A-2',
                   'Printer:Canon': 'A-3',
                   'Scaner:Canon': 'B-1',
                   'Scaner:Epson': 'B-2',
                   'Xserox:Xserox': 'C-1',
                   'Xserox:Epson': 'C-2'
                 }

    def __init__(self, number, adres, phone):
        self.number = number
        self.adres = adres
        self.phone = phone
        self.list_params = [[]]
        self.cells_technics = defaultdict(list)

    def store_input(self, object_technic: Technics, total):
        today = datetime.date.today()
        list_input = []

        object_technic.take_in(total)

        file_log = open('store_log.txt', 'a')
        str_log = f"{today} {object_technic.type_technic} {total}"
        with file_log:
            file_log.write(str_log + '\n')

        list_input.extend([object_technic.type_technic, object_technic.serial_number,
                           object_technic.model, object_technic.producer]
                         )

        self.list_params.append(list_input)

    def store_out(self, object_technic: Technics, total):
        object_technic.take_out(total)

        file_log = open('store_log.txt', 'a')
        str_log = f"{datetime.date.today()} {object_technic.type_technic} -{total}"
        with file_log:
            file_log.write(str_log + '\n')

    def store_rests(self):
      Technics.get_rests()

    def move_technics_cells(self):
        for el_list in self.list_params[1:]:
            cell = f"{el_list[0]}:{el_list[3]}"
            cell = StoreTechnics.dict_cells[cell]
            self.cells_technics[cell].append(el_list[2])
        return self.cells_technics

# Техника
printer_001 = Printer('Printer', 'PP_004', 'Laser', 'modelAXX', 5690, 20, True, 'лазерный')
printer_002 = Printer('Printer', 'PP_009', 'HP', 'modelHP78', 7900, 12, False, 'струйный')
printer_003 = Printer('Printer', 'PP_741', 'HP', 'modelSS78', 5690, 20, True, 'матричный')
printer_004 = Printer('Printer', 'PP_9630', 'Canon', 'modelCC_100', 27900, 48, False, '3D')

scaner_001 = Scaner('Scaner', 'SS_125', 'Canon', 'V370', 25000, 'планшетный', 19, 600 )
scaner_002 = Scaner('Scaner', 'SS_7844', 'Epson', 'DR-F120', 19000, 'барабанный', 42, 750)
scaner_003 = Scaner('Scaner', 'SS_200', 'Epson', 'M-345S', 32000, '3D', 55, 750)

xserox_001 = Xserox('Xserox', 'XX_300', 'Xserox', 'xx_78100', 45000, True, 'A4')
xserox_002 = Xserox('Xserox', 'XX_700', 'Epson', 'FXX_45200', 17100, False, 'A1')

#Склад
store_0001 = StoreTechnics('№789', 'Складская 45/4', '84995564238')

print(f"Прием техники на склад {store_0001.number} по адресу {store_0001.adres}")
# Принять технику на склад
store_0001.store_input(printer_001, 4)
store_0001.store_input(printer_002, 8)
store_0001.store_input(printer_003, 15)
store_0001.store_input(printer_004, 9)

store_0001.store_input(scaner_001, 10)
store_0001.store_input(scaner_002, 7)
store_0001.store_input(scaner_003, 15)

store_0001.store_input(xserox_001, 2)
store_0001.store_input(xserox_002, 6)

# Остатки на складе
print('*********Остатки после приемки*********')
store_0001.store_rests()

# размещение товаров на складе
print('*********Размещение товара*********')
print(dict(store_0001.move_technics_cells()))

# списани товаров
print('*********Списание товара*********')
try:
    store_0001.store_out(printer_001, 6)
    store_0001.store_out(scaner_003, 3)
except ValueError as error:
    print(error)

# Остатки на складе
print('*********Остатки после списания*********')
store_0001.store_rests()


