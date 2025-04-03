import csv

class Item:
    #to store all the inputs in a list
    all = []
    pay_rate = 0.8 #polymorphism
    def __init__(self, name: str, price: float, quantity: int):
        # running input validations
        assert price >= 0, "Price must be positive!"
        assert quantity>= 0, "Quantity must be positive!"
        # storing input data
        self.__name = name
        self.__price = price
        self.quantity = quantity
        # to store the input in the list
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    # polymorphism
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    # encapsulation
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # this is a getter
    @property
    # property decorator = read-only attribute
    def name(self):
        return self.__name

    # this is a setter
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name must be less than 10 characters!")
        else:
            self.__name = value

    def calculate_total_price(self):
     return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name= item.get('name'),
                price= float(item.get('price')),
                quantity= int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # it counts all floats (including those that are point zero)
        if isinstance(num, float):
            # counts out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}:( {self.name}, price: {self.__price}, quantity: {self.quantity})"

    def __connect(self, smtp):
        pass

    def __prepare_body(self):
        print(f'''
        Dear customer,
        We have {self.__name} which are {self.quantity} in number and they go for {self.__price}.
        Best regards, Kahoro.
        ''')
        pass

    def __send(self):
        pass

    # abstraction
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
