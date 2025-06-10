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
    - a list of dictionaries containing each product from the csv
    - number of products in each category
    - the time the inventory was created
'''

class ProductManager:
    def __init__(self, file_name, log_time):
        self._inventory = []
        self._file_name = file_name
        self._log_time = log_time

    #setter methods:
    def set_file_name(self, f):
        self.file_name = f
    def set_log_time(self, l):
        self._log_time = l

    #getter methods:
    def get_file_name(self):
        return self._file_name
    def get_log_time(self):
        return self._log_time
    def get_inventory(self):
        pass


    '''
    To string method that will display all product information for testing a visualization purposes
    To string format:
    
    '''
    def __str__(self):
        pass

