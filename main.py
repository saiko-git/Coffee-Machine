# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 13:24:08 2025

@author: ahmed amr ahmed khalil
"""
from CoffeeMachine import CoffeeMachine
from Resources import Resources
from Customer import Customer
###Initialization of the resources
espresso = Resources("espresso")
latte = Resources("latte")
cappuccino = Resources("cappuccino")
coffee_machine = CoffeeMachine()

def Processing(drink):
    print(f"the {drink.name} costs ${drink.money}")
    if(coffee_machine.IsSufficient(drink)):
        customer = Customer(drink)
        customer.ProcessCoins()
        if(customer.IsTransactionSuccessful()):
            coffee_machine.MakeCoffee(drink)
            print(f"Enjoy your {drink.name}")
print("################################################################################")
###Input of the user
while(True):
    choice = input("“What would you like? (espresso/latte/cappuccino): ")
    while(choice != "espresso" and choice != "latte" and choice != "cappuccino" and choice != "off" and choice != "report" ):
        choice = input("We don't have your choice,please choose one of the drinks we offer: ")
    else:
        if(choice == "espresso"):
            Processing(espresso)
            
        elif(choice == "latte"):
            Processing(latte)
            
        elif(choice == "cappuccino"):
            Processing(cappuccino)
                    
        elif(choice == "report"):
            coffee_machine.PrintReport()
        else:
            break
    

    
        
    
        
    
    
