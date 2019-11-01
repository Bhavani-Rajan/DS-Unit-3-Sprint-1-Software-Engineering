#!/usr/bin/env python
from random import randint, sample, uniform
import numpy as np
from acme import Product


# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):

    products = []
    len_adj = len(ADJECTIVES)
    len_noun = len(NOUNS)
    # TODO - your code! Generate and add random products.
    for i in range(num_products):

        name = sample(ADJECTIVES,1)[0] + ' ' + sample(NOUNS,1)[0]
        price = randint(5,100)
        weight = randint(5,100)
        flammability =uniform(0.0,2.5)
        prod = Product(name,price,weight,flammability)
        products.append(prod)

    return products




def inventory_report(products):
        """Generate the report for the inventory of products"""


        # TODO - your code! Loop over the products to calculate the report.
        len_prod_list = len(products)
        names=[]
        wt = []
        price = []
        flammability = []

        """
        populate the list to generate the report
        """
        for i in range(len_prod_list):
            names.append(products[i].name)
            wt.append(products[i].weight)
            price.append(products[i].price)
            flammability.append(products[i].flammability)

        print('-------------------------------------------')
        print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
        print('-------------------------------------------')
        print('Unique product names: ',len(np.unique(names)))
        print('Average price: ',np.round(np.mean(price),2))
        print('Average weight: ',np.mean(wt))
        print('Average flammability: ',np.mean(flammability))
        print('-------------------------------------------')

if __name__ == '__main__':
    inventory_report(generate_products())
