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

    test = ProductManager("copy_csv_shawn.csv", "00:00")

    print(test.get_file_name())

    #test.load_data()
    inventory = test.load_data()

    product = Product()

    product.convert_data(inventory)





if __name__ == "__main__":
    main()