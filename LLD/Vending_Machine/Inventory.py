from Item import Item
from ItemShelf import ItemShelf

class Inventory:

    def __init__(self, item_count: int):
        self.inventory = [None] * item_count
        self.initial_empty_inventory()

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

    def initial_empty_inventory(self):
        start_code = 101
        for i in range(len(self.inventory)):
            space = ItemShelf()
            space.set_code(start_code)
            space.set_sold_out(True)
            self.inventory[i] = space
            start_code += 1

    def add_item(self, item: 'Item', code_number: int):
        for item_shelf in self.inventory:
            if item_shelf.code == code_number:
                if item_shelf.is_sold_out():
                    item_shelf.item = item
                    item_shelf.set_sold_out(False)
                else:
                    raise Exception("already item is present, you can not add item here")

    def get_item(self, code_number: int) -> 'Item':
        for item_shelf in self.inventory:
            if item_shelf.code == code_number:
                if item_shelf.is_sold_out():
                    raise Exception("item already sold out")
                else:
                    return item_shelf.item
        raise Exception("Invalid Code")

    def update_sold_out_item(self, code_number: int):
        for item_shelf in self.inventory:
            if item_shelf.code == code_number:
                item_shelf.set_sold_out(True)
