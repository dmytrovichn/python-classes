

class Product:
    WEIGHT_TYPES = ['кг', 'г', 'ц']

    def __init__(self, name, price, weight_type='кг'):
        if weight_type not in self.WEIGHT_TYPES:
            raise TypeError("Wrong weight type")
        self.__name = name
        self.__price = float(price)
        self.__weight_type = weight_type

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def weight_type(self):
        return self.__weight_type

    @weight_type.setter
    def weight_type(self, weight_type):
        self.set_weight_type(weight_type)

    def __str__(self):
        return f'{self.__name}: {self.__price} грн/{self.__weight_type}'

    def check_weight_type(self, weight_type):
        if weight_type not in self.WEIGHT_TYPES:
            raise TypeError("Wrong weight type")

    def set_weight_type(self, weight_type):
        self.check_weight_type(weight_type)
        if self.__weight_type == weight_type:
            return

        if self.__weight_type == 'кг' and weight_type == 'г':
            self.__weight_type = weight_type
            self.__price = self.__price / 1000

        if self.__weight_type == 'г' and weight_type == 'кг':
            self.__weight_type = weight_type
            self.__price = self.__price * 1000

        if self.__weight_type == 'кг' and weight_type == 'ц':
            self.__weight_type = weight_type
            self.__price = self.__price * 100

        if self.__weight_type == 'ц' and weight_type == 'кг':
            self.__weight_type = weight_type
            self.__price = self.__price / 100

        if self.__weight_type == 'г' and weight_type == 'ц':
            self.__weight_type = weight_type
            self.__price = self.__price * 100000

        if self.__weight_type == 'ц' and weight_type == 'г':
            self.__weight_type = weight_type
            self.__price = self.__price / 100000

    def __mul__(self, percent):
        return Product(self.__name, self.__price + self.__price * (percent/100), self.__weight_type)

