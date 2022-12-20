# Лабораторная работа №6, вариант 5

class Disc:

    # Поля: объем, кол-во оборотов в минуту, ширина лазера, тип диска (CD или DVD)
    def __init__(self, capacity, rpm, laserWidth, type=''):
        self.Capacity = capacity
        self.RPM = rpm
        self.LaserWidth = laserWidth
        self.Type = type

    # Метод выводит строку с параметрами диска
    def __str__(self):
        return f'Оптический {self.Type} диск\n{self.Capacity} МБ\n{self.RPM} об./мин\n{self.LaserWidth} нм'

    # Метод, подсчитывающий среднее время одного оборота диска
    def avg(self):
        avg_time = round(1000 / (self.RPM / 60), 2)
        return avg_time

    # Метод, подсчитывающий кол-во байт которые считывает лазр за 20 сек
    # если принять что скорость считывания лазера ~150 Кб/с
    def BytesPer20s(self):
        bytes = 20 * 150000
        return bytes

    # Метод, складывающий объем двух дисков одного типа
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.Capacity + other.Capacity
        else:
            raise TypeError("Не могу добавить {1} к {0}".
                            format(self.__class__, type(other)))

# Подкласс CD дисков
class CD(Disc):

    # Инициализатор имеет дополнительно поле относительно родительского класса
    def __init__(self, capacity, rpm, laserWidth, type, writeable):
        Disc.__init__(self, capacity, rpm, laserWidth, type)
        if writeable == 1:
            self.Writeable = 'Чтение и запись'
        elif writeable == 0:
            self.Writeable = 'Только чтение'
        else:
            self.Writeable = 'unknown'

    # Метод __str__ в подклассах переопределены чтобы выводить уникальные для них поля
    def __str__(self):
        return f'Оптический {self.Type} диск\n{self.Capacity} МБ\n{self.RPM} об./мин\n{self.LaserWidth} нм\n{self.Writeable}'

# Подкласс CD дисков
class DVD(Disc):

    # Инициализатор имеет дополнительно поле относительно родительского класса
    def __init__(self, capacity, rpm, laserWidth, type, doubleSided):
        Disc.__init__(self, capacity, rpm, laserWidth, type)
        if doubleSided == 1:
            self.DoubleSided = 'Двусторонний'
        elif doubleSided == 0:
            self.DoubleSided = 'Односторонний'
        else:
            self.DoubleSided = 'unknown'

    # Метод __str__ в подклассах переопределены чтобы выводить уникальные для них поля
    def __str__(self):
        return f'Оптический {self.Type} диск\n{self.Capacity} МБ\n{self.RPM} об./мин\n{self.LaserWidth} нм\n{self.DoubleSided}'

    # Переопределяю метод, так как скорость считываения DVD диска в 9 раз больше чем у CD
    def BytesPer20s(self):
        bytes = 20 * 150000 * 9
        return bytes

# Несколько примеров использования объектов и методов созданных классов
test = Disc(7100, 7200, 780,)
testcd = CD(3400, 5600, 780, "CD", 0)
testdvd = DVD(10400, 10000, 650, 'DVD', 0)
print(testdvd.__str__())
print(test.__add__(testcd))
print(testdvd.avg())
