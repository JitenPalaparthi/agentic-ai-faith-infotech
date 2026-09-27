class Inventory:
    def __init__(self):
        self.stock = {}
    def add(self, sku, qty):
        self.stock[sku] = self.stock.get(sku, 0) + qty
    def remove(self, sku, qty):
        if self.stock.get(sku, 0) < qty:
            raise ValueError("insufficient stock")
        self.stock[sku] -= qty

inv = Inventory()
inv.add("P1", 10)
inv.remove("P1", 3)
print(inv.stock)
