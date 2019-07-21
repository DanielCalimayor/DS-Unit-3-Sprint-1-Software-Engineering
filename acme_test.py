#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from acme import Product
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealable_explodey(self):
        prod = Product('EXPLOSIVE Dynamite', 1000, 1, 100)
        self.assertEqual(prod.explode(), 'HUGE explostion')
        self.assertEqual(prod.stealability(), 'very stealable!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()
        adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

        for product in products:
            prod_name = product.name.split()
            adjective = prod_name[0]
            

