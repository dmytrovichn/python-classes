from product import Product


class Order(Product):

    def __init__(self, name, price, count, weight_type='кг'):
        super().__init__(name, price, weight_type)
        self.__count = count

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def __str__(self):
        return f'{super().__str__()} : {self.__count} {self.weight_type} : price = {self.count_sum()}'

    def set_weight_type(self, weight_type):
        self.check_weight_type(weight_type)
        if self.weight_type == 'кг' and weight_type == 'г':
            self.__count = self.__count * 1000

        if self.weight_type == 'г' and weight_type == 'кг':
            self.__count = self.__count / 1000

        if self.weight_type == 'кг' and weight_type == 'ц':
            self.__count = self.__count / 100

        if self.weight_type == 'ц' and weight_type == 'кг':
            self.__count = self.__count * 100

        if self.weight_type == 'г' and weight_type == 'ц':
            self.__count = self.__count / 100000

        if self.weight_type == 'ц' and weight_type == 'г':
            self.__count = self.__count * 100000
        super().set_weight_type(weight_type)

    def count_sum(self):
        return self.__count * self.price

    def __ge__(self, other):
        return self.count_sum() >= other.count_sum()


class Orders:

    def __init__(self, elements=None):
        self.__elements = elements if elements else []

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, count):
        self.__elements = count

    def add(self, element):
        self.__elements.append(element)

    def __str__(self):
        check = ['--------------------', 'Orders Description:', '--------------------']
        for order in self.__elements:
            check.append(order.__str__())
        check.append(f'--------------------\n Total price: {self.total_sum()}\n--------------------')

        return '\n'.join(check)

    def __add__(self, other):
        self.__elements = self.__elements + other
        return Orders(self.__elements)

    def total_sum(self):
        total_sum = 0
        for order in self.__elements:
            total_sum += order.count_sum()
        return total_sum






