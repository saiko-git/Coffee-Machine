# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 13:24:09 2025

@author: ahmed amr ahmed khalil
"""
from Resources import Resources
class CoffeeMachine:
    def __init__(self):
        self.coffee_machine = Resources("coffeemachine")
        self.money = self.coffee_machine.money
        
    def PrintReport(self):
        print("the current resource values are:")
        print(f"Water: {self.coffee_machine.water}ml")
        print(f"Milk: {self.coffee_machine.milk}ml")
        print(f"Coffee: {self.coffee_machine.coffee}g")
        print(f"Money: ${self.coffee_machine.money}")
        
    def IsSufficient(self,resource):
        if(resource.water > self.coffee_machine.water):
            print("Sorry there is not enough water")
            return False
        elif(resource.milk > self.coffee_machine.milk):
            print("Sorry there is not enough milk")
            return False
        elif(resource.coffee > self.coffee_machine.coffee):
            print("Sorry there is not enough coffee")
            return False
        else:
            return True
        
    def MakeCoffee(self,drink):
        self.coffee_machine.money += drink.money
        self.coffee_machine.water -= drink.water
        self.coffee_machine.milk -= drink.milk
        self.coffee_machine.coffee -= drink.coffee
        
        
        
        

