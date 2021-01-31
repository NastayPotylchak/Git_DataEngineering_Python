# Класс Комплексные числа

class ComplexNumber:
    def __init__(self, part_real, part_imag):
        self.part_real = part_real
        self.part_imag = part_imag

    def __str__(self):
      return str(complex(self.part_real, self.part_imag))

    def __add__(self, other):
        result = complex(self.part_real, self.part_imag) + complex(other.part_real, other.part_imag)
        return ComplexNumber(result.real, result.imag)

    def __mul__(self, other):
        s_real = self.part_real
        s_imag = self.part_imag

        o_real = other.part_real
        o_imag = other.part_imag

        result_real = s_real*o_real - s_imag*o_imag
        result_imag = s_imag*o_real + s_real*o_imag

        return ComplexNumber(result_real, result_imag)

complex_number1 = ComplexNumber(2, 3)
complex_number2 = ComplexNumber(1, 4)
complex_number3 = ComplexNumber(8, 0)

number_add = complex_number1 + complex_number2 + complex_number3
print(number_add)

complex_number4 = ComplexNumber(1, 1)
complex_number5 = ComplexNumber(1, 4)

number_mul = complex_number4 * complex_number5
print(number_mul)
