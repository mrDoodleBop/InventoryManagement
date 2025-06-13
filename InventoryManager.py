'''
File Name : InventoryManager.py
Author Name : Michael Cates
Date : 6/12/2025
Purpose :
'''

#imports:
import ProductManager
from ProductManager import ProductManager
import Product
from Product import Product


def main():

    #dictionary containing the keywords required for categorization
    word_dict = {
        # Category 1
        "SSCOPE / LIGHT / LASER": [
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

    test = ProductManager("copy_csv_shawn.csv", "00:00")

    print(test.get_file_name())

    """
    To Do (6/13/2025) :
        - break down current convert_data function into three individual functions for abstraction
        - the function that removes t-shirts and patches should be re-written to ask the user what products they would 
            like to remove based on keyword
        - create new method that uses the cleaned list of dictionaries to set values to each Product class attribute
        - *** work on multi-row products in the csv file (will most likely require changes in the ProductManager class:
            -> this process should most likely be done as the inventory data is read in by ProductManager
    """
    test.load_data()
    test.clean_data(word_list, word_dict)
    product_list = test.load_objects()


    for product in product_list:
        print(product)






if __name__ == "__main__":
    main()