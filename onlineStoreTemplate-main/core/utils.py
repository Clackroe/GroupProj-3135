import sqlite3



def dict_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    """
    Creates a dictionary from a row in the database. This is used to convert the rows into dictionaries.

    args:
        - cursor: The cursor of the database, which is a built-in sqlite3 class.
        - row: The row to convert into a dictionary.

    returns:
        - The dictionary of the row.
    """

    row_dict = {}
    for index, column in enumerate(cursor.description):
        row_dict[column[0]] = row[index]
    return row_dict

# Add compare_cost method below
# Add compare_mileage below
# Calculate cost based on price, * 1 + taxrate, pull price from db when Nate is done, remove discount and quantity
def calculate_cost(price: int, tax_rate: float = 0.05) -> float:
    """
    Calculates the cost of an item.

    args:
        - vin: Vin number of vehicle being purchased.
        - tax_rate: The tax rate of the item.

    returns:
        - The cost of the item as a float.
    """
    return price * (1 + tax_rate)

def compare_cost(price1: int, price2: int):
    """
    Compares any two vehicles by price for customers to view which they prefer to purchase
    
    args:
        - price1: Price number of vehicle 1
        - price2: Price number of vheicle 2

    returns:
        - Make and model of the cheaper vehicle
    """
    if (price1 < price2):
            cheapestPrice = price1
    else:
         cheapestPrice = price2

    return cheapestPrice

def compare_mileage(miles1: int, miles2: int):
    """
    Compares any two vehicles by mileage for customers to view which they prefer to purchase
    
    args:
        - miles1: Mileage of vehicle 1
        - miles2: Mileage of vheicle 2

    returns:
        - Make and model of the cheaper vehicle
    """
    if (miles1 < miles2):
            lowestMiles = miles1
    else:
        lowestMiles = miles2
        

    return lowestMiles


# Want to add sorting methods for Make, Body Style, and lowest to highest prices, highest to lowest prices
# Need to speak with Xander and Nate on how to do so in a way that changes the html and if I need to do something differnt here
# in order to do so
# Basically how to make these methods in here reactive with the webpage

def sortByMake():
     pass

def sortByBodyStyle():
     pass

def pricesLowToHigh():
     pass

def pricesHighToLow():
     pass

