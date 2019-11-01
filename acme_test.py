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



if __name__ == '__main__':
    unittest.main()
