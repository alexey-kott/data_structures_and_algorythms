class NonNegative:
    # def __init__(self, name: str):
    #     self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        print(name)
        self.name = name


class Order:
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, price, quantity):
        # self.price = price
        # self.quantity = quantity
        pass


order = Order(100, 10)
order.price = 100
# print(order.price)
