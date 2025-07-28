# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 13:24:10 2025

@author: ahmed amr ahmed khalil
"""
class Customer:
    def __init__(self,drink):
        self.drink = drink
        self.coins = 0
    def ProcessCoins(self):
        print("please insert the coins")
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        self.coins = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
        
        
    def IsTransactionSuccessful(self):
        if(self.coins < self.drink.money):
            print("That is not enough money, money refunded")
            return False
        if(self.coins > self.drink.money):
            print(f"Here is ${round(self.coins-self.drink.money,2)} in change")
        return True
            
            
            
            
        
        
    
        

