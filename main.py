from item import Item
from phone import Phone
from chair import Chair

# Item.instantiate_from_csv()
# print(Item.all)

#if you are running Phone add broken_phone argument
item1 = Chair("Kahoro", 750, 1)
item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)
item1.send_email()
