'''
File Name : InventoryManager.py
Author Name : Michael Cates
Date : 6/12/2025
Purpose :
'''

#imports:
from bs4 import BeautifulSoup
import requests

import ProductManager
from ProductManager import ProductManager
import Product
from Product import Product

from CSV_Manager import CSV_Manager
#from CSV import CSV


def main():

    #dictionary containing the keywords required for categorization
    word_dict = {
        # Category 1
        "SCOPE / LIGHT / LASER": [
            "scope",
            "optic",
            "laser"
        ],
        # Category 2
        "PYROTECHNICS / SMOKES": [
            "grenade",
            "projectile",
            "smoke",
            "tag-19"
        ],
        # Category 3
        "PARTS": [
            "magazine",
            "grip",
            "mount",
            "grease"
        ],
        # Category 4
        "MISC / TRINKETS": [
            "marker",
            "plate",
            "converter"
        ],
        # Category 5
        "HPA": [
            "station",
            "device",
            "chassis",
            "launcher",
            "version"
        ],
        # Category 6
        "GEARS / GLOVES / CLOTHES": [
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
        # Category 7
        "GAS / BBS / BATTERIES": [
            "BB's",
            "Cartridge"
        ],

        # Category 8
        "AIRSOFT SNIPERS / DMR": [
            "sniper",
            "dmr"
        ],
        # Category 9
        "AIRSOFT RIFLES": [
            "rifle"
        ],
        # Category 10
        "AIRSOFT PISTOLS": [
            "pistol"
        ],
        # Category 11
        "AIRSOFT LMG": [
            "lmg"
        ]
    }  # end of keyword dictionary

    # list containing keywords for removal
    word_list = [
        "patch",
        "t-shirt",
        "tshirt"
    ]  # end of keyword list

    #list of Product objects
    product_list = []

    test = CSV_Manager("https://airsoftstation.com", "00:00")

    test.load_data()
    
    #print(test)
    #first_item = next(iter(test.get_inventory().items()))
    
    '''
    for sub_cat, child_cat in first_item[1].items():
        print("\n\n\n{}".format(sub_cat))
        for child_cat, value in child_cat.items():
            print("    {}".format(child_cat))
            print("        {}".format(value))
    '''

    #test.load_urls_csv()







if __name__ == "__main__":
    main()