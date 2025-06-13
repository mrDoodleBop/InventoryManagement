'''
File Name : ProductManager.py
Author Name : Michael Cates
Date : 6/9/2025
Purpose : This file is where the data will be loaded and stored from the product CSV file
'''

#imports
from datetime import datetime

import csv
from csv import DictReader


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
        self._inventory = [] #list of dictionaries containing all products and their information
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
    Load data method to load all products and their attributes from the csv file into a list of dictionaries
        It should open the csv file and create a reader object
        It should then load a dictionary with the information from a row of the csv file
        It should then add the dictionary to the inventory list
        It should repeat this process for the entirety of the csv file
    '''
    def load_data(self):

        with open(self._file_name, encoding='utf-8-sig', errors='replace') as data:

            reader = DictReader(data)

            for row in reader:

                # dictionary containing all information for a single product from the csv file
                product_dict = {
                    "Name": row.get("Name", ""),
                    "Code": row.get("Code", ""),
                    "Brand": row.get("Brand", ""),
                    "Price": row.get("MAP Price", ""),
                    "Warranty": row.get("Warranty", ""),
                    "Weight": row.get("Weight", ""),
                    "Stock Level": row.get("Stock Level", ""),
                    "Product Images": row.get("Product Images", ""),
                    "UPC/EAN": row.get("UPC/EAN", "")
                }

                print("Dictionary created")

                # add new dictionary to the list of products
                self._inventory.append(product_dict)

                print("Dictionary added to inventory list")
            print(product_dict)
            print(self._inventory)


    '''
    To string method that will display all product information for testing a visualization purposes
    To string format:
    
    '''
    def __str__(self):
        pass

