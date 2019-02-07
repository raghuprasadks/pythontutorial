class Product():
#class Product(object):
    def __init__(self, price, item_name, weight, brand, status='For Sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, tax):
        return "Price after sales tax: ${}".format(self.price * (1 + (tax/100.0)))

    def return_item(self, reason_for_return):
        if reason_for_return.lower() == 'defective':
            self.status = 'Defective'
            self.price = 0
        elif reason_for_return.lower() == 'like new':
            self.status = 'For Sale'
        elif reason_for_return.lower() == 'open box':
            self.status = 'Used'
            self.price = 0.8 * self.price # 20% discount
        return self

    def display_all(self):
        print ("Price: ${}".format(self.price))
        print ("Item Name:", self.item_name)
        print ("Weight: {}g".format(self.weight))
        print ("Brand:", self.brand)
        print ("Status:", self.status)
        return self

chocolate = Product(5, 'chocolate', 100, 'Dairy Milk')

print ("Initial Specs: ")
chocolate.display_all()

print ("Specs after adding tax: ")
print (chocolate.add_tax(15))

print ("Specs after selling: ")
chocolate.sell().display_all()

print ("Specs after returning: ")
chocolate.return_item('defective').display_all()