# Object-Oriented Programming Assignment / Assignment 2 Programming Principles
# 2023-11-10
# Jeremy Tica

class product:
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, estimated_monthly_units):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost =  manufacture_cost
        self.stock_level = stock_level
        self.estimated_monthly_units = estimated_monthly_units

    def show(self):
        print(self.code)
        print(self.name)
        print(self.sale_price)
        print(self.manufacture_cost)
        print(self.stock_level)
        print(self.estimated_monthly_units)

product_one = product(900, "Rice", 1000000, 1337, 2, 37)
product_one.show()