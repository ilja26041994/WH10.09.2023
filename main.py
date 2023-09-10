# # Создать класс Тг1апа]е для представления треугольника. Поля данных долж-
# # ны включать углы и стороны. Требуется реализовать операции: получения
# # и изменения полей данных, вычисления площади, вычисления периметра,
# # вычисления высот, а также определения вида треугольника (равносторонний,
# # равнобедренный или прямоугольный).
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_area(self):
#         p = (self.a + self.b + self.c) / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c
#
#     def get_height(self):
#         return self.a * self.b * self.c / (self.a + self.b + self.c)
#
#     def get_type(self):
#         if self.a == self.b and self.b == self.c:
#             return "равносторонний"
#         elif self.a == self.b or self.b == self.c or self.a == self.c:
#             return "равнобедренный"
#         elif self.a ** 2 + self.b ** 2 == self.c ** 2 or self.a ** 2 + self.c ** 2 == self.b ** 2 or self.b ** 2 + self.c ** 2 == self.a ** 2:
#             return "прямоугольный"
#         else:
#             return "произвольный"
#
# sideOfTheTriangle1 = int(input('Введите сторону 1: '))
# sideOfTheTriangle2 = int(input('Введите сторону 2: '))
# sideOfTheTriangle3 = int(input('Введите сторону 3: '))
#
# triangle = Triangle(sideOfTheTriangle1, sideOfTheTriangle2, sideOfTheTriangle3)
# print(triangle.get_area())
# print(triangle.get_perimeter())
# print(triangle.get_height())
# print(triangle.get_type())

# # Создать класс Мопеу для работы с денежными суммами. Число должно быть
# # представлено двумя полями: типа long для рублей и типа unsigned char — для
# # копеек. Дробная часть (копейки) при выводе на экран должна быть отделена
# # от целой части запятой. Реализовать сложение, вычитание, деление сумм,
# # деление суммы на дробное число, умножение на дробное число и операции
# # сравнения.
#
# class Money:
#     def __init__(self, rub, kop):
#         self.rub = rub
#         self.kop = kop
#
#     def __str__(self):
#         return f'{self.rub} руб. {self.kop} коп.'
#
#     def __add__(self, other):
#         return Money(self.rub + other.rub, self.kop + other.kop)
#
#     def __sub__(self, other):
#         return Money(self.rub - other.rub, self.kop - other.kop)
#
#     def __mul__(self, other):
#         return Money(self.rub * other.rub, self.kop * other.kop)
#
#     def __truediv__(self, other):
#         return Money(self.rub // other.rub, self.kop // other.kop)
#
#     def __eq__(self, other):
#         return self.rub == other.rub and self.kop == other.kop
#
#     def __gt__(self, other):
#         return self.rub > other.rub or self.kop > other.kop
#
#     def __lt__(self, other):
#         return self.rub < other.rub or self.kop < other.kop
#
#     def __ge__(self, other):
#         return self.rub >= other.rub and self.kop >= other.kop
#
#     def __le__(self, other):
#         return self.rub <= other.rub and self.kop <= other.kop
#
#     def __ne__(self, other):
#         return self.rub != other.rub or self.kop != other.kop
#
# money11 = int(input('Введите количество рублей: '))
# money12 = int(input('Введите количество копеек: '))
# money21 = int(input('Введите количество рублей: '))
# money22 = int(input('Введите количество копеек: '))
# print(Money(money11, money12))
# print(Money(money21, money22))
# try:
#     summ = Money.__add__(Money(money11, money12), Money(money21, money22))
#     print('Сумма:', summ)
#     difrence = Money.__sub__(Money(money11, money12), Money(money21, money22))
#     print('Разность:', difrence)
#     product = Money.__mul__(Money(money11, money12), Money(money21, money22))
#     print('Произведение:', product)
#     dividingAmounts = Money.__truediv__(Money(money11, money12), Money(money21, money22))
#     print('Частное:', dividingAmounts)
#     comparison1 = Money.__eq__(Money(money11, money12), Money(money21, money22))
#     print('Равенство:', comparison1)
#     comparison2 = Money.__ne__(Money(money11, money12), Money(money21, money22))
#     print('не равенство:', comparison2)
#     comparison3 = Money.__gt__(Money(money11, money12), Money(money21, money22))
#     print('больше:', comparison3)
#     comparison4 = Money.__ge__(Money(money11, money12), Money(money21, money22))
#     print('больше или равно:', comparison4)
#     comparison5 = Money.__le__(Money(money11, money12), Money(money21, money22))
#     print('меньше или равно:', comparison5)
#     comparison6 = Money.__lt__(Money(money11, money12), Money(money21, money22))
#     print('меньше:', comparison6)
# except Exception:
#     print('Ошибка')


# # Реализовать класс Bankomat, моделирующий работу банкомата. В классе должны
# # содержаться поля для хранения идентификационного номера банкомата,
# # информации о текущей сумме денег, оставшейся в банкомате, минимальной и
# # максимальной суммах, которые позволяется снять клиенту в один день.
# # Сумма денег представляется полями-номиналами 10-1000.
# # Реализовать метод инициализации банкомата, метод загрузки купюр в банкомат
# # и метод снятия определенной суммы денег. Метод снятия денег должен выполнять
# # проверку на корректность снимаемой суммы: она не должна быть
# # меныше минимального значения и не должна превышать максимальное значение.
# # Метод toString() должен преобразовать в строку сумму денег, оставшуюся в банкомате.
#
# class Bankomat:
#     def __init__(self, number, money, min, max):
#         self.indentification_number = number
#         self.available_money = money
#         self.min = min
#         self.max = max
#
#     def load_money(self, money):
#         self.available_money += money
#         if self.available_money < self.min:
#             self.available_money = self.min
#         if self.available_money > self.max:
#             self.available_money = self.max
#
#     def take_money(self, money):
#         self.available_money -= money
#         if self.available_money < self.min:
#             self.available_money = self.min
#         if self.available_money > self.max:
#             self.available_money = self.max
#
#     def __str__(self):
#         return f'Банкомат No{self.indentification_number},' \
#                f' сумма денег: {self.available_money} руб.' \
#                f' {self.available_money // 100} коп.'
# try:
#     theAmountOfMoneyAvailableAtTheATM = int(input('Введите сумму денег в банкомате: '))
#     theATMBankomat = Bankomat(1, theAmountOfMoneyAvailableAtTheATM, 1000, 1000000)
#     print(theATMBankomat)
# except Exception:
#     print('Ошибка создания банкомата')
# try:
#     incosatingMoney = int(input('Введите сумму денег которую хотите внести в банкомат: '))
#     theATMBankomat.load_money(incosatingMoney)
#     print(theATMBankomat)
# except Exception:
#     print('Ошибка загрузки денег')
# try:
#     theMoneyFromATMBankomat = int(input('Введите сумму денег которую хотите снять с банкомата: '))
#     theATMBankomat.take_money(theMoneyFromATMBankomat)
#     print(theATMBankomat)
# except Exception:
#     print('Ошибка снятия денег')
# print(theATMBankomat.__str__())