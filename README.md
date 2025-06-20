# Inventory Management

## Problem Statement
This program accepts a CSV file containing new and/ or existing products for the GruntPa Tactical website and allows the user to complete a number of inventory management tasks that simplifies future data handling and manipulation.

The program will accept an inital CSV and eventually return a new, more organized, CSV file.

## Iteration 1
### For the first iteration of this program, the user should be able to complete these tasks:
1. **Add and/ or delete** specific products from the CSV file
2. **Simplify product image URLs** into a list of individual URLs (this process will be checked and/ or completed automatically by the program)
       a. the current URLs are stung together in one line, separated by delimeters
#### Classes to be created
1. **Product Class:**
   - This class will be the blueprint telling the program how to store the data from the CSV
   - Each product row will be turned into an object instance of this class
2. **Product Manager Class:**
   - This class will be where the data from the CSV file will be loaded and stored into a list of dictionaries
          - each dictionary in the list will contain all information required to create a Product object that can be worked with in the future
## Iteration 2
### For th second iteration of this program, the user should be able to complete these tasks:
1. **Scrape the airsoftstation.com website for data on all products to put into a csv file
2. **Using the csv file generated from the website, complete all tasks from Iteration 1

### Classes to be created   
1. **CSV Manager Class**
   - This class will be where the data from the website is loaded and stored into a dictionary
   - It will load the data from the website into an organized dictionary
   - It will then load the data into a csv to allow for future use of the data




