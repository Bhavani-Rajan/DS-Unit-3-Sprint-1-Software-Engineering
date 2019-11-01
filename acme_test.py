#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """ Test default product weight being 20. """
        prod1 = Product('Product One')
        self.assertEqual(prod1.weight, 20)

    def test_stealability(self):
        """ Test stealability equals Very stealable """
        prod2 = Product('Product Two',21)
        self.assertEqual(prod2.stealability(),'Very stealable!')

    def test_explode(self):
        """ Test explode equals baboom """
        prod3 = Product('Product Three',price=10,weight=50,flammability = 1.1)
        self.assertEqual(prod3.explode(),'...BABOOM!!')

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """ Test the default number of products is being 30"""
        self.assertEqual(len(generate_products()),30)

    def test_legal_names(self):
        """ Test the names of products are valid from the list """
        ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        prod_list = generate_products()
        names_list = []

        for i in range(len(prod_list)):
            names_list.append(prod_list[i].name)

        for x in range(len(names_list)):
            name_split = names_list[x].split()
            self.assertIn(name_split[0],ADJECTIVES)
            self.assertIn(name_split[1],NOUNS)

if __name__ == '__main__':
    unittest.main()
