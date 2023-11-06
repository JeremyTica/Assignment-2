# Object-Oriented Programming Assignment / Assignment 2 Programming Principles
# 2023-11-10
# Jeremy Tica
import random
import os 

class Product:
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, estimated_monthly_units):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost =  manufacture_cost
        self.stock_level = stock_level
        self.estimated_monthly_units = estimated_monthly_units

    def show(self):
        print("Product Code:", self.code)
        print("Product Name:", self.name)
        print("Product Cost: $"+str(self.sale_price)+ " CAD")
        print("Manufacture Cost: $"+str(self.manufacture_cost)+ " CAD")
        print("Initial Stock:", self.stock_level)
        print("Estimate monthly production:", self.estimated_monthly_units)

    def product_sales(self):
        #! Initial Stock
        print("\nMonth 1")
        number_of_units_sold = 10 * random.randint(1,10)
        print(number_of_units_sold, "Units Sold")
        stock_difference = self.stock_level + self.estimated_monthly_units - number_of_units_sold
        print("Current Stock:", stock_difference)

        total_units_sold = number_of_units_sold
        total_units_manufactured = self.estimated_monthly_units

        for months in range(1, 12):
            print("\nMonth", months+1)

            stock_difference += self.estimated_monthly_units #! Units being produced monthly 
            total_units_manufactured += self.estimated_monthly_units

            if stock_difference <= 0:
                total_units_sold += number_of_units_sold + stock_difference
                print("Out of Stock!")
                break
            else:
                number_of_units_sold = 10 * random.randint(1,10) 

                stock_difference -= number_of_units_sold
                if stock_difference <= 0: #! Under the condition that the stock goes under 0, it will ask the user whether or not they wish to sell the remaining stock from the previous month, and the stock produced from the current month
                    while True:
                        accept_sale = input("Not enough stock! Sell remaining stock anyways? [yes/no]: ")
                        if accept_sale == "yes":
                            print("Accepting Sale...")
                            stock_difference += number_of_units_sold #! Redo calculation
                            number_of_units_sold = stock_difference #! Sell the rest of the stock
                            print("Selling remaining", number_of_units_sold, "units...")
                            break #! Break this loop
                        elif accept_sale == "no":
                            print("Declining Sale...")
                            number_of_units_sold = 0
                            break
                        else:
                            print("Please choose a valid option!")
                    if accept_sale: #! Break outer loop
                        total_units_sold += number_of_units_sold
                        break
                else:
                    total_units_sold += number_of_units_sold
                    print(number_of_units_sold, "Units Sold")
                    print("Current Stock:", stock_difference)

        print("\n\nTotal Units Sold:", total_units_sold)
        print("Total Stock Produced: ", total_units_manufactured)
        
        net_profit = total_units_sold * self.sale_price - total_units_manufactured * self.manufacture_cost
        print("Net-profit: $", format(net_profit,".2f"))

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
        p_sale_price = float(input("\nPlease input the product sale price: "))
        if p_sale_price > 0:
            ask_product_manufacture_cost()
            break
        else:
            print("Please enter a valid product sale price")

def ask_product_manufacture_cost():
    while True:
        global p_manufacture_cost
        p_manufacture_cost = float(input("\nPlease input the product manufacture cost: "))
        if p_manufacture_cost > 0:
            ask_stock_level()
            break
        else:
            print("Please enter a valid product manufacture cost")

def ask_stock_level():
    while True:
        global p_stock_level
        p_stock_level = int(input("\nPlease input the current product stock level: "))
        if p_stock_level > 0:
            ask_estimated_monthly_units_manufactured()
            break
        else:
            print("Please enter a valid stock level")

def ask_estimated_monthly_units_manufactured():
    while True:
        global p_estimated_monthly_units
        p_estimated_monthly_units = int(input("\nPlease input the estimate of units that will be manufactured monthly: "))
        if p_estimated_monthly_units >= 0:
            os.system("cls")
            break
        else:
            print("Please enter a valid estimate of units that will be manufactured monthly:")


#! Program Call
ask_product_code()

#! Class Call
product_one = Product(p_code, p_name, p_sale_price, p_manufacture_cost, p_stock_level, p_estimated_monthly_units)

#! Product Information
product_one.show()

#! Product Sales Overview
product_one.product_sales()
