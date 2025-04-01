class Item:
    pay_rate=0.8
    #to store all the inputs in a list
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        # running input validations
        assert price >= 0, "Price must be positive!"
        assert quantity>= 0, "Quantity must be positive!"
        # storing input data
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"I have {quantity} {name} which are valued at {price} each.")
        # to store the input in the list
        Item.all.append(self)
    def calculate_total_price(self):
     return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    def __repr__(self):
        return f"Item:( {self.name}, price: {self.price}, quantity: {self.quantity})"

item1 = Item("car", 1500,6)
item2 = Item("phone", 800, 8)
item3 = Item("chair",700,10)
item4 = Item("desk",1000,5)
item5 = Item("shoe", 200,2)
print(Item.all)
