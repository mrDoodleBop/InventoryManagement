'''
File Name : Product.py
Author Name : Michael Cates
Date : 6/9/2025
Purpose :
'''

#imports
import csv


'''
The Product class for a single product from the csv file
The class should contain:
    - the product name : str
    - the product SKU code : str
    - the product brand : str
    - the product map price : float
    - the product warranty : str
    - the product weight : float
    - the product stock_level : int
    - the product image urls : list[str]
    - the product "upc_ean" : str
'''

class Product:
    def __init__(self, name, code, brand, price, warranty, weight, stock_level, image_urls, upc_ean):
        self._name = name
        self._code = code
        self._brand = brand
        self._price = price
        self._warranty = warranty
        self._weight = weight
        self._stock_level = stock_level
        self._image_urls = image_urls
        self._upc_ean = upc_ean

        #Variable for the list of separated urls
        self._image_list = []


    #setter methods:
    def set_name(self, n):
        self._name = n
    def set_code(self, c):
        self._code = c
    def set_brand(self, b):
        self._brand = b
    def set_price(self, p):
        self._price = p
    def set_warranty(self, wr):
        self._warranty = wr
    def set_weight(self, wt):
        self._weight = wt
    def set_stock_level(self, s):
        self._stock_level = s
    def set_image_urls(self, i):
        self._image_urls = i
    def set_upc_ean(self, u):
        self._upc_ean = u
    def set_image_list(self, image_list):
        self._image_list = image_list

    #getter methods:
    def get_name(self):
        return self._name
    def get_code(self):
        return self._code
    def get_brand(self):
        return self._brand
    def get_price(self):
        return self._price
    def get_warranty(self):
        return self._warranty
    def get_weight(self):
        return self._weight
    def get_stock_levels(self):
        return self._stock_level
    def get_image_urls(self):
        return self._image_urls
    def get_upc_ean(self):
        return self._upc_ean
    def get_image_list(self):
        return self._image_list


    '''
    Method that is passed a dictionary and turns the entries into Product objects
        - format the image urls
            -> turn one long string (with delimiters) into a list of strings
        - format the pricing to go two decimal spaces
        - if stock is not populated or 0 say "Out of Stock"
        - 
    '''
    def convert_data(self, product_dict):
        pass