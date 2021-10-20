class InvalidQuantityException(Exception):
    pass

class cls_inventory:
    def __init__(self,limit=100):
        self.__limit = limit
        self.__total_items = 0

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
    @property
    def total_items(self):
        return self.__total_items

    @total_items.setter
    def total_items(self, value):
        self.__total_items = value

    def add_new_stock(self, name, price, quantity):
        if quantity <= 0:
            raise InvalidQuantityException(f'Cannot add a quantity of {quantity}. All new stocks must have at least 1 item')
        else:
            self.__total_items += quantity
    def remove_stock(self, item, quantity):
            self.__total_items -= quantity
