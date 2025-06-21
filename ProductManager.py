'''
File Name : ProductManager.py
Author Name : Michael Cates
Date : 6/9/2025
Purpose : This file is where the data will be loaded and stored from the product CSV file
'''

#imports
from datetime import datetime
from collections import defaultdict
import csv
from csv import DictReader
import Product
from Product import Product


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

        self._image_list = []

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
        return self._inventory

    '''
    Load data method to load all products and their attributes from the csv file into a list of dictionaries
        It should open the csv file and create a reader object
        It should then load a dictionary with the information from a row of the csv file
        It should then add the dictionary to the inventory list
        It should repeat this process for the entirety of the csv file
    '''
    def load_data(self):
        # Dictionary to store products grouped by their SKU
        grouped_products = defaultdict(list)
        
        with open(self._file_name, encoding='utf-8-sig', errors='replace') as data:
            reader = DictReader(data)
            
            for row in reader:
                # Use the product Code (SKU) as the identifier
                sku = row.get("Code", "").strip()
                
                # Create product dictionary for this row
                product_dict = {
                    "Name": row.get("Name", ""),
                    "Code": sku,
                    "Brand": row.get("Brand", ""),
                    "Price": row.get("MAP Price", ""),
                    "Warranty": row.get("Warranty", ""),
                    "Weight": row.get("Weight", ""),
                    "Stock Level": row.get("Stock Level", ""),
                    "Product Images": row.get("Product Images", ""),
                    "UPC/EAN": row.get("UPC/EAN", ""),
                    "Configuration": row.get("Configuration", "")  # Add configuration field if it exists
                }

                #print("Dictionary created")

                # add new dictionary to the list of products
                self._inventory.append(product_dict)

                #print("Dictionary added to inventory list")
            #print(product_dict)
            #print(self._inventory)

    '''
    Methods that clean the inventory data for future use
        1. rmv_products
        2. cat_products
        3. format_urls
    '''

    # function to remove products from the inventory by keyword
    def rmv_products_by_keyword(self, keyword):

        for item in self._inventory:

            if keyword.lower() in item["Name"].lower():
                # remove item
                self._inventory.remove(item)

    #function to remove products from the inventory by a list of keywords
    def rmv_products_by_list(self, keywords):
        # iterate through each item in the inventory
        for item in self._inventory:

            # iterate through the list of removal words for search:
            for keyword in keywords:

                if keyword.lower() in item["Name"].lower():
                    # remove the product from the list
                    self._inventory.remove(item)

    # function to categorize all products in the inventory using a dictionary of lists containing category keywords:
    def cat_products(self, categories):

        for item in self._inventory:

            for category, words, in categories.items():

                for word in words:

                    if word.lower() in item["Name"].lower():
                        item["Category"] = category
                        break

                if "Category" in item:
                    break

    # function to split the image URLs into a list of indidivual URLs
    def format_urls(self):

        for item in self._inventory:
            # format the image urls

            image_field = item.get("Product Images", "")
            images = image_field.replace("Product Image URL: ", "").split("|")

            self._image_list.append(images)
            #print(images)

    #function to complete all the tasks above in one go, if needed
    def clean_data(self, keywords, categories):

        self.rmv_products_by_list(keywords)
        self.cat_products(categories)
        self.format_urls()



    '''
    Load object method that uses the inventory list of dictionaries and turns the entries into a product class objects
    RETURNS : a list of Product class objects
    '''
    def load_objects(self):

        product_list = []
        i = 0
        for item in self._inventory:

            new_product = Product(
                item.get("Name"),
                item.get("Code"),
                item.get("Brand"),
                item.get("Price"),
                item.get("Warranty"),
                item.get("Weight"),
                item.get("Stock Level"),
                self._image_list[i],
                item.get("UPC/EAN")
            )

            product_list.append(new_product)
            #print("{} has been added to the list of products.".format(new_product.get_name()))
            i += 1
        return product_list
