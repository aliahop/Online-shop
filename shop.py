class Shop():
    def __init__(self, shop_name, store_type) :
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0
    def describe_shop(self):
        print(self.shop_name)
        print(self.store_type)
    def open_shop(self):
        print(self.shop_name + ' is open now')
    def count(self):
        print('This shop has ' + str(self.number_of_units) + ' units')
    def count_update(self, pcs):
        self.number_of_units = pcs
class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products
    def get_discounts_products(self):
        return self.discount_products


store = Shop('Sinsay', 'clothes')
print(store.shop_name.title())
print(store.store_type.title())
store.describe_shop()
store.open_shop()
print(store.count())
store.count_update(25)
print(store.count())

store1 = Shop('Allo', 'phones')
store2 = Shop('Eva', 'cosmetics')
store1.describe_shop()
store2.describe_shop()

store_discount = Discount('Reserved', 'clothe', 'T-shirt, trousers')
store_discount.describe_shop()
print(store_discount.get_discounts_products())