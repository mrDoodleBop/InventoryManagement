'''
File Name : CSV_Manager.py
Author Name : Michael Cates
Date : 6/16/2025
Purpose :
'''

from math import prod
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import csv

'''
CSV manager class should load and store all product data from a website
It should also store the inventory generation time
It should contain:
    - a dictionary containing a dictionary containing a list of products, categorized correctly for the csv file
    - the number of products in each major category
    - the time the inventory was created
'''

class CSV_Manager:
    def __init__(self, website_url, log_time):

        self._inventory = {} #main dictionary for the overall inventory
        self._website_url = website_url
        self._log_time = log_time

        #set up the key and value variables for the inventory dictionary
        self._main_category = None
        self._sub_category = None
        self._child_category = None
        self._url = None

    #setter methods:
    def set_website_url(self, url):
        self._website_url = url

    def set_log_time(self, lt):
        self._log_time = lt

    def set_inventory(self, dict):
        self._inventory = dict

    #getter methods:
    def get_website_url(self):
        return self._website_url

    def get_log_time(self):
        return self._log_time

    def get_inventory(self):
        return self._inventory

    '''
    Load data method to load all products and their attributes from the website
        1. It needs to open the homepage of the website to scrape through each product category and pull the url for the category page
        2. Loop through each category url, open that url, pull product information and store it properly
        3. Return a dictionary containing all categorized products, their attributes, and the link for each product
    '''
    def load_data(self):

        # Make a request to the website
        response = requests.get(self._website_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Successfully opened {self._website_url} (Status: {response.status_code})")
            
            # Get the HTML content
            html_content = response.content
            
            # Parse the HTML with BeautifulSoup
            soup = BeautifulSoup(html_content, "html.parser")
            
            # Message to the user that the website was opened successfully
            print("\n\nWebsite opened successfully. Ready to scrape product data.")

            '''
            The program now needs to scrape the website for the following information:
                 - Main Category
                 - Sub Category
                 - Child Category
                 - All child category urls

            The program will store this information into the inventory dictionary, with the following format:
            {
                "Main Category": {
                    "Sub Category": {
                        "Child Category": "URL"
                    }
                }
            }

            
            Begin by accessing the product category list
            The following tags will need to be accessed (in this order):
                 - body class="deafult"
                 - header class="header header_fixed"
                 - div class="header_middle"
                 - div class="header_m_right"
                 - div class="navPages-container"
                 - nav class="navPages"
                 - ul class="navPages-list"
                      -> this is where the list of main categories can be found
                      -> make sure to skip accessing the "Deals" section

                      - a class="navPages-action has-subMenu"
                           -> this is where the name of the main category can be found (the aria-label)

                      - div class="navPage-subMenu"
                      - ul class="navPage-subMenu-list"
                           -> this is where the list of sub categories can be found
                           -> make sure to skip accessing the following sub categories:
                                - "All Airsoft Guns"
                                - "Canada Legal Airsoft Guns"
                                - "New Arrivals"

                           - a class="navPage-subMenu-action navPages-action has-subMenu"
                                ->this is where the name of the sub category can be found (the aria-label)
                                - ul class"navPage-childList"
                                     -> this is where the list of child categories can be found
                                     - li class="navPage-childList-action navPages-action"
                                     - a class="navPage-childList-action navPages-action"
                                         -> this is where the name of the child category can be found (the aria-label)
                                         -> this is where the url of the child category can be found (the href)
            '''



 
        else:
            print(f"Failed to open {self._website_url} (Status: {response.status_code})")
            return None


    def load_urls_csv(self):
        '''
        Writes the urls from the inventory dictionary into a new CSV file.
        Each row: Main Category, Sub Category, Child Category, URL
        '''
        with open("inventory_urls.csv", "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Main Category", "Sub Category", "Child Category", "URL"])
            #iterate through the main category of the inventory dictionary
            for main_cat, sub_dict in self._inventory.items():
                #iterate through the sub category of the main category
                for sub_cat, child_dict in sub_dict.items():
                    #if the child dictionary is a dictionary, iterate through it
                    if isinstance(child_dict, dict):
                        for child_cat, url in child_dict.items():
                            writer.writerow([main_cat, sub_cat, child_cat, url])
                    else:
                        # If child_dict is not a dict, treat sub_cat as child_cat
                        writer.writerow([main_cat, sub_cat, sub_cat, child_dict])

    '''
    To string method to return the inventory, in an easy to read format, for testing purposes
    '''
    def __str__(self):
        '''
        Formatting for output:
        
        Main-Category:

            Sub-Category:

                Child-Category1:
                Child-Category2:
                ...
                Child-CategoryN:
            ...
            Sub-CategoryN:
        '''
        output = []
        if self._inventory:
            main_cat, sub_dict = next(iter(self._inventory.items()))
            output.append(f"\n\n\n{main_cat}:")
            for sub_cat, child_dict in sub_dict.items():
                output.append(f"    \n\n{sub_cat}:")
                if isinstance(child_dict, dict):
                    for child_cat, value in child_dict.items():
                        output.append(f"        \n{child_cat}: {value}")
                else:
                    output.append(f"       \n {child_dict}")
        else:
            output.append("Inventory is empty.")
        return '\n'.join(output)

        
