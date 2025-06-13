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

        #Variable to store the category the product belongs to
        self._category = ""


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
    def get_image_list(self):
        return self._image_list
    def get_category(self):
        return self._category


    '''
    Method that is passed a list of dictionaries and turns the entries into Product objects
        - format the image urls
            -> turn one long string (with delimiters) into a list of strings
        - format the pricing to go two decimal spaces
        - if stock is not populated or 0 say "Out of Stock"
        - 
    Parameter(s): inventory (list of dictionaries containing all the required information to create a Product object
    Returns: a list of Product objects
    '''
    def convert_data(self, inventory):

        '''
        SEARCH BY KEYWORD:
            This section of the program will complete two tasks:
                1. Remove all T-Shirts and Patches from the inventory, as they will no longer be sold on the airsoft website
                2. Categorize all inventory products, according to the organizational requirements of the airsoft website

        A dictionary of keywords (for categorization) and list of keywords (for data removal) will first be created, allowing for easier/ more efficient search
        The program will then iterate through the list of dictionaries, cross-referencing each product name with each keyword:
            - If the name contains the word t-shirt or patch, the product will be removed from the inventory
            - Otherwise, the program will then begin to iterate through the dictionary of keywords to find the keyword that
                appears in the product name and categorize it accordingly based on that keyword's dictionary key
        '''

        #dictionary containing keywords required for categorization
        word_dict = {
            #Category 1
            "SSCOPE / LIGHT / LASER" : [
                "scope",
                "optic",
                "laser"
            ],
            #Category 2
            "PYROTECHNICS / SMOKES" : [
                "grenade",
                "projectile",
                "smoke",
                "tag-19"
            ],
            #Category 3
            "PARTS" : [
                "magazine",
                "grip",
                "mount",
                "grease"
            ],
            #Category 4
            "MISC / TRINKETS" : [
                "marker",
                "plate",
                "converter"
            ],
            #Category 5
            "HPA" : [
                "station",
                "device",
                "chassis",
                "launcher",
                "version"
            ],
            #Category 6
            "GEARS / GLOVES / CLOTHES" : [
                "glove",
                "panel",
                "goggles",
                "hat",
                "mask",
                "rig",
                "sling",
                "scarf",
                "rag",
                "holster"
            ],
            #Category 7
            "GAS / BBS / BATTERIES" : [
                "BB's",
                "Cartridge"
            ],

            #Category 8
            "AIRSOFT SNIPERS / DMR" : [
                "sniper",
                "dmr"
            ],
            #Category 9
            "AIRSOFT RIFLES" : [
                "rifle"
            ],
            #Category 10
            "AIRSOFT PISTOLS" : [
                "pistol"
            ],
            #Category 11
            "AIRSOFT LMG" : [
                "lmg"
            ]
        }#end of keyword dictionary

        #list containing keywords for removal
        word_list = [
            "patch",
            "t-shirt",
            "tshirt"
        ]#end of keyword list

        #iterate through each item in the inventory
        for item in inventory:

            #iterate through the list of removal words for search:
            for word in word_list:

                if word in item["Name"].lower():

                    #remove the product from the list
                    inventory.remove(item)
                    print("A {} has been removed from the inventory.".format(word.upper()))

            #now that all required products have been removed from the inventory, the remaining products can be categorized
            #search through every word in the word_dict, and if any of the words in word_dict are in the name of the current item in inventory, set the category attribute of the Product object to the word's dictionary key:
            for Category, word in word_dict.items():
                for w in word:
                    if w.lower() in item["Name"].lower():
                        item["Category"] = Category
                        print("{} has been categorized to {}.".format(item["Name"], Category))
                        break

                if "Category" in item:
                    break


            # format the image urls
            '''
            image_field = item.get("Product Images", "")
            self._image_list = [img.replace("|Product Image URL: ", "").strip() for img in image_field.split(",") if img.strip()]
            #self._image_list = [img.replace("|", "").strip() for img in image_field.split(",") if img.strip()]


            print(self._image_list)
            '''

            image_field = item.get("Product Images", "")
            self._image_list = image_field.replace("Product Image URL: ", "").split("|")

            print(self._image_list)








