'''
File Name : ProductManager.py
Author Name : Michael Cates
Date : 6/9/2025
Purpose : This file is where the data will be loaded and stored from the product CSV file
'''

#imports
from datetime import datetime

import Product


'''
The ProductManager class should load and store all product data from a csv file. 
It should also store the inventory generation time. 
It should contain:
    - a dictionary of Product object lists - key = product category & value = list of products in that category
    - number of products in each category
    - the time the inventory was created
'''

class ProductManager:
    def __init__(self, file_name, log_time):
        self._inventory = {}
        self._file_name = file_name
        self._log_time = log_time

    #setter methods:

    #getter methods: