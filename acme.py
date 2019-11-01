"""
Class to represent the Product that amce manages and sells
"""
from random import randint

class Product:
    """
    This is the generic representation of Product
    """
    def __init__(self,name,price=10,weight=20,flammability = 0.5):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000,9999999)

    def stealability(self):
        msg = ''
        ratio_price_wt = self.price / self.weight
        if(ratio_price_wt < 0.5):
            msg = 'Not so stealable...'
        elif(ratio_price_wt >= 0.5 and ratio_price_wt < 1.0):
            msg = 'Kinda stealable.'
        else:
            msg = 'Very stealable!'

        return msg

    def explode(self):
        msg = ''
        flammability_x_wt = self.flammability * self.weight
        if(flammability_x_wt < 10):
            msg ='...fizzle.'
        elif(flammability_x_wt >= 10 and flammability_x_wt < 50):
            msg ='...boom!'
        else:
            msg='...BABOOM!!'
        return msg

class BoxingGlove(Product):
    """
    This is BoxingGlove, a type of Product
    """
    def __init__(self,name,weight=10):
        super().__init__(name)
        self.weight = weight

    def explode(self):
        msg = "...it's a glove."
        return msg

    def punch(self):
        msg=''
        if(self.weight < 5):
            msg='That tickles.'
        elif(self.weight >= 5 and self.weight < 15):
            msg='Hey that hurt!'
        else:
            msg='OUCH!'
        return msg
