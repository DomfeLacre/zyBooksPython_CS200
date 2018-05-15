class ItemToPurchase:
    """
    (1) Build the ItemToPurchase class with the following specifications:

    Attributes (3 pts)
        item_name (string)
        item_price (float)
        item_quantity (int)
    Default constructor (1 pt)
        Initializes item's name = "none", item's price = 0, item's quantity = 0
    Method
        print_item_cost()
    """

    def __init__(self, item_name=str(None), item_price=float(0), item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def calc_cost(self):
        price = self.item_price
        quantity = self.item_quantity
        total = price * quantity

    def print_item_cost(self):
        return print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity,
                                                int(self.item_price),
                                                int(self.item_price * self.item_quantity)))

    def __add__(self, other):
        combo_cost = self.calc_cost() + other.calc_cost()
        return combo_cost


item1 = ItemToPurchase()
print("Item 1")
item1.item_name = input("Enter the item name: ")
item1.item_price = input("Enter the item price: ")
item1.item_quantity = input("Enter the item quantity: ")

print("\n")

item2 = ItemToPurchase()
print("Item 2")
item2.item_name = input("Enter the item name: ")
item2.item_price = input("Enter the item price: ")
item2.item_quantity = input("Enter the item quantity: ")

print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

print("Total: $".format(item1 + item2))
