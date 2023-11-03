# Object-Oriented Programming Assignment / Assignment 2 Programming Principles
# 2023-11-10
# Jeremy Tica

class Product:
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

def ask_product_code():
    while True:
        global p_code
        p_code = int(input("\nPlease input the product code: "))
        if p_code >= 100 and p_code <= 1000:
            ask_product_name()
            break
        else:
            print("Please enter a valid product code within 100-1000")

def ask_product_name():
    while True:
        global p_name
        p_name = input("\nPlease input the product name: ")
        ask_product_sale_price()
        break

def ask_product_sale_price():
    while True:
        global p_sale_price
        p_sale_price = int(input("\nPlease input the product sale price: "))
        if p_sale_price > 0:
            ask_product_manufacture_cost()
            break
        else:
            print("Please enter a valid product sale price")

def ask_product_manufacture_cost():
    while True:
        global p_manufacture_cost
        p_manufacture_cost = int(input("\nPlease input the product manufacture cost: "))
        if p_manufacture_cost > 0:
            ask_stock_level()
            break
        else:
            print("Please enter a valid product manufacture cost")

def ask_stock_level():
    while True:
        global p_stock_level
        p_stock_level = int(input("\nPlease input the product stock level: "))
        if p_stock_level > 0:
            ask_estimated_monthly_cost()
            break
        else:
            print("Please enter a valid stock level")

def ask_estimated_monthly_cost():
    while True:
        global p_estimated_monthly_cost
        p_estimated_monthly_cost = int(input("\nPlease input the estimated monthly cost: "))
        if p_estimated_monthly_cost >= 0:
            break
        else:
            print("Please enter a reasonable monthly cost estimate")


ask_product_code()
product_one = Product(p_code, p_name, p_sale_price, p_manufacture_cost, p_stock_level, p_estimated_monthly_cost)
product_one.show()