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
    #Loaded constructor
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

        #Variable to store the category the product belongs to
        self._category = "Uncategorized"

    '''
    #Default constructor
    def __init__(self):
        self._name = "N/A"
        self._code = "N/A"
        self._brand = "N/A"
        self._price = 0.0
        self._warranty = "N/A"
        self._weight = 0.0
        self._stock_level = 0
        self._image_urls = "N/A"
        self._upc_ean = "N/A"

        # Variable for the list of separated urls
        self._image_list = []

        # Variable to store the category the product belongs to
        self._category = "Uncategorized"
    '''

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
    def set_category(self, category):
        self._category = category

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
    def get_category(self):
        return self._category


    '''
    To string method that will display all product information for testing a visualization purposes
    To string format:
    ----------------------------
    Name : 
    Code : 
    Brand : 
    Price : 
    Warranty : 
    Weight : 
    Stock Level : 
    Product Images : 
    UPC/EAN :
    ----------------------------
    '''
    def __str__(self):

        return "\n-------------Product---------------\nName : {}\nCode : {}\nBrand : {}\nPrice : {}\nWarranty : {}\nWeight : {}\nStock Level : {}\nProduct Images : {}""\nUPC/EAN : {}\n-------------------------------------".format(self._name, self._code, self._brand, self._price, self._warranty, self._weight, self._stock_level, self._image_urls, self._upc_ean)







