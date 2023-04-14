import sqlite3
from database.db import Database


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
def calculate_cost(vin: int, tax_rate: float = 0.05) -> float:
    """
    Calculates the cost of an item.

    args:
        - vin: Vin number of vehicle being purchased.
        - tax_rate: The tax rate of the item.

    returns:
        - The cost of the item as a float.
    """
    return Database.get_vehicle_price_by_vin(vin) * (1 + tax_rate)

def compare_cost(vin1: int, vin2: int):
    """
    Compares any two vehicles by price for customers to view which they prefer to purchase
    
    args:
        - vin1: Vin number of vehicle 1
        - vin2: Vin number of vheicle 2

    returns:
        - Make and model of the cheaper vehicle
    """

    price1 = Database.get_vehicle_price_by_vin(vin1)
    price2 = Database.get_vehicle_price_by_vin(vin2)
    cheapestPrice

    if (price1 < price2):
            cheapestPrice = price1
    else:
         cheapestPrice = price2

    return cheapestPrice

def compare_mileage(vin1: int, vin2: int):
    """
    Compares any two vehicles by price for customers to view which they prefer to purchase
    
    args:
        - vin1: Vin number of vehicle 1
        - vin2: Vin number of vheicle 2

    returns:
        - Make and model of the cheaper vehicle
    """

    miles1 = Database.get_vehicle_mileage_by_vin(vin1)
    miles2 = Database.get_vehicle_mileage_by_vin(vin2)
    lowestMiles

    if (miles1 < miles2):
            lowestMiles = miles1
    else:
        lowestMiles = miles2

    return lowestMiles


