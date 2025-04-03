from item import Item

class Chair(Item):
    pay_rate = 0.7 #polymorphism
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)