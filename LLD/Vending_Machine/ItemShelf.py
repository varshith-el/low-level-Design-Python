from Item import Item

class ItemShelf:
    def __init__(self):
        self.code = None
        self.item = None
        self.sold_out = None

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_item(self):
        return self.item

    def set_item(self, item: 'Item'):
        self.item = item

    def is_sold_out(self):
        return self.sold_out

    def set_sold_out(self, sold_out: bool):
        self.sold_out = sold_out
