from item import Item

class Phone(Item):
    pay_rate = 0.9 #polymorphism
    def __init__(self, name: str, price: float, quantity: int, broken_phones: int):
        super().__init__(name, price, quantity)
        # running input validations
        assert broken_phones >= 0, "Number of broken phones must be positive!"
        # storing input data
        self.broken_phones = broken_phones

phone1=Phone("Samsung", 350, 6, 2)
