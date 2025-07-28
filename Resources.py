# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 13:57:28 2025

@author: ahmed amr ahmed khalil
"""

class Resources:
    def __init__(self,resource):
        water = float(input(f"Enter the amount of water in ml for the {resource}: "))
        milk = float(input(f"Enter the amount of milk in ml for the {resource}: "))
        coffee = float(input(f"Enter the amount of coffee beans in grams for the {resource}: "))
        self.name = resource
        self.water = water
        self.milk = milk
        self.coffee = coffee
        if(resource.lower() == "coffeemachine"):
            self.money = 0
        else:
            self.money = float(input(f"Eneter the price of the {resource} in $: "))