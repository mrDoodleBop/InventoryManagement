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
                 - body class="default"
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

            # More efficient approach: Try to find the navigation list directly
            navPages_list = soup.find("ul", class_="navPages-list")
            
            if navPages_list is None:
                print("Could not find navigation list (navPages-list). Trying alternative approach...")
                # Try to find any navigation structure
                navPages_list = soup.find("ul", {"class": "navPages-list"})
                if navPages_list is None:
                    print("Could not find any navigation structure. Exiting.")
                    return None

            print("Successfully found navigation structure. Starting to extract categories...")

            # Debug: Print the first few elements to see the actual structure
            print(f"\nDEBUG: Found {len(navPages_list.find_all('li'))} list items in navigation")
            
            # Try to find any main category links to see what's actually there
            all_main_links = navPages_list.find_all("a")
            print(f"DEBUG: Found {len(all_main_links)} anchor tags in navigation")
            
            for i, link in enumerate(all_main_links[:5]):  # Show first 5 links
                print(f"DEBUG: Link {i+1}: classes={link.get('class', 'No class')}, aria-label={link.get('aria-label', 'No aria-label')}")

            # Define categories to skip
            skip_main_categories = ["Deals"]
            skip_sub_categories = ["All Airsoft Guns", "Canada Legal Airsoft Guns", "New Arrivals"]

            # Find all main category items
            main_categories = navPages_list.find_all("li", recursive=False)
            
            for main_category_item in main_categories:
                try:
                    # Find main category link - try multiple approaches
                    main_category_link = main_category_item.find("a", class_="navPages-action has-subMenu")
                    
                    # If that doesn't work, try alternative searches
                    if main_category_link is None:
                        print(f"DEBUG: No 'navPages-action has-subMenu' found, trying alternatives...")
                        # Try just navPages-action
                        main_category_link = main_category_item.find("a", class_="navPages-action")
                        
                    if main_category_link is None:
                        # Try any anchor tag
                        main_category_link = main_category_item.find("a")
                        
                    if main_category_link is None:
                        print(f"DEBUG: No anchor tag found in main category item")
                        continue

                    # Debug: Print what we found
                    print(f"DEBUG: Found link with classes: {main_category_link.get('class', 'No class')}")
                    print(f"DEBUG: aria-label: {main_category_link.get('aria-label', 'No aria-label')}")
                    
                    main_category_name = main_category_link.get("aria-label", "Unknown Category")
                    
                    # If still unknown, try other attributes
                    if main_category_name == "Unknown Category":
                        # Try text content
                        main_category_name = main_category_link.get_text(strip=True)
                        if not main_category_name:
                            # Try title attribute
                            main_category_name = main_category_link.get("title", "Unknown Category")
                    
                    print(f"DEBUG: Final category name: {main_category_name}")
                    
                    # Skip unwanted main categories
                    if main_category_name in skip_main_categories:
                        print(f"Skipping main category: {main_category_name}")
                        continue

                    print(f"\nProcessing main category: {main_category_name}")

                    # Initialize sub-categories dictionary for this main category
                    sub_categories = {}

                    # Find submenu
                    submenu = main_category_item.find("div", class_="navPage-subMenu")
                    if submenu is None:
                        self._inventory[main_category_name] = sub_categories
                        continue

                    # Find submenu list
                    submenu_list = submenu.find("ul", class_="navPage-subMenu-list")
                    if submenu_list is None:
                        self._inventory[main_category_name] = sub_categories
                        continue

                    # Process sub-categories
                    sub_category_items = submenu_list.find_all("li", recursive=False)
                    
                    for sub_category_item in sub_category_items:
                        try:
                            # Find sub-category with submenu
                            sub_with_submenu = sub_category_item.find("a", class_="navPage-subMenu-action navPages-action has-subMenu")
                            if sub_with_submenu is None:
                                continue

                            sub_category_name = sub_with_submenu.get("aria-label", "Unknown Sub-Category")
                            
                            # Skip unwanted sub-categories
                            if sub_category_name in skip_sub_categories:
                                print(f"  Skipping sub-category: {sub_category_name}")
                                continue

                            print(f"  Processing sub-category: {sub_category_name}")

                            # Initialize child categories dictionary
                            child_categories = {}

                            # Find child list
                            child_list = sub_category_item.find("ul", class_="navPage-childList")
                            if child_list is None:
                                sub_categories[sub_category_name] = child_categories
                                continue

                            # Process child categories
                            child_items = child_list.find_all("li", class_="navPage-childList-item")
                            
                            for child_item in child_items:
                                try:
                                    # Find child category link
                                    child_link = child_item.find("a", class_="navPage-childList-action navPages-action")
                                    if child_link is None:
                                        continue

                                    child_category_name = child_link.get("aria-label", "Unknown Child Category")
                                    child_url = child_link.get("href", "")
                                    
                                    if child_url:
                                        child_categories[child_category_name] = child_url
                                        print(f"    Found child category: {child_category_name}")

                                except Exception as e:
                                    print(f"    Error processing child category: {e}")
                                    continue

                            # Add sub-category and its children to the main category
                            sub_categories[sub_category_name] = child_categories

                        except Exception as e:
                            print(f"  Error processing sub-category: {e}")
                            continue

                    # Add main category and its sub-categories to the inventory
                    self._inventory[main_category_name] = sub_categories

                except Exception as e:
                    print(f"Error processing main category: {e}")
                    continue

            print(f"\nScraping completed. Found {len(self._inventory)} main categories.")
            
            # Write the inventory to text file to view the contents for testing purposes
            self.write_inventory_to_text()
            self.load_urls_csv()
            
            return self._inventory
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
            writer.writerow(["Main-Category", "Sub-Category", "Child-Category", "Product-Page-URL"])
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

    def write_inventory_to_text(self):
        '''
        Writes the complete inventory dictionary to a text file in a readable format.
        Creates a hierarchical view of all categories and their URLs.
        '''
        with open("inventory_structure.txt", "w", encoding='utf-8') as file:
            file.write("INVENTORY STRUCTURE\n")
            file.write("=" * 50 + "\n\n")
            
            if not self._inventory:
                file.write("Inventory is empty.\n")
                return
            
            for main_cat, sub_dict in self._inventory.items():
                file.write(f"MAIN CATEGORY: {main_cat}\n")
                file.write("-" * 30 + "\n")
                
                if not sub_dict:
                    file.write("  No sub-categories found.\n\n")
                    continue
                
                for sub_cat, child_dict in sub_dict.items():
                    file.write(f"  SUB-CATEGORY: {sub_cat}\n")
                    
                    if isinstance(child_dict, dict):
                        if not child_dict:
                            file.write("    No child categories found.\n")
                        else:
                            for child_cat, url in child_dict.items():
                                file.write(f"    CHILD CATEGORY: {child_cat}\n")
                                file.write(f"    URL: {url}\n")
                    else:
                        # If child_dict is not a dict, treat sub_cat as child_cat
                        file.write(f"    URL: {child_dict}\n")
                    
                    file.write("\n")
                
                file.write("\n" + "=" * 50 + "\n\n")
            
            # Add summary at the end
            file.write("SUMMARY\n")
            file.write("-" * 20 + "\n")
            file.write(f"Total Main Categories: {len(self._inventory)}\n")
            
            total_sub_categories = 0
            total_child_categories = 0
            
            for sub_dict in self._inventory.values():
                total_sub_categories += len(sub_dict)
                for child_dict in sub_dict.values():
                    if isinstance(child_dict, dict):
                        total_child_categories += len(child_dict)
                    else:
                        total_child_categories += 1
            
            file.write(f"Total Sub-Categories: {total_sub_categories}\n")
            file.write(f"Total Child Categories: {total_child_categories}\n")
            file.write(f"Inventory Generation Time: {self._log_time}\n")
            file.write(f"Website URL: {self._website_url}\n")

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

