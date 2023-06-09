from database.db import Database
from core.utils import dict_factory


def test_init_db(db: Database = None) -> tuple:
    """
    Tests that the database is initialized correctly.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db") if db is None else db

    if db.database_path != "database/storeRecords.db":
        error = f"Error in test_init_db: Database path is not correct.\n  - Actual: {db.database_path}"
        return False, error
    else:
        return True, "Database path is correct."


def test_get_inventory_exists(db: Database = None) -> tuple:
    """
    Tests that the inventory is not empty.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/storeRecords.db") if db is None else db
    full_inventory = db.get_full_inventory()

    if len(full_inventory) == 0:
        error = f"Error in test_get_full_inventory: Full inventory is empty.\n  - Actual: {len(full_inventory)}"
        return False, error
    else:
        return True, "Full inventory is not empty."


def test_dict_factory_link(db: Database = None) -> tuple:
    """
    Tests that the row factory is linked to dict_factory.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    db = Database("database/storeRecords.db") if db is None else db
    row_factory = db.connection.row_factory

    if row_factory != dict_factory:
        error = f"Error in test_dict_factory_link: Row factory is not linked to dict_factory.\n  - Expected: {dict_factory}\n  - Actual: {row_factory}"
        return False, error
    else:
        return True, "Row factory is linked to dict_factory."


def test_check_connection_threaded(db: Database = None) -> tuple:
    """
    Tests that the database connection is not single threaded.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """

    db = Database("database/storeRecords.db") if db is None else db
    connection_is_threaded = db.connection.isolation_level is None

    if connection_is_threaded:
        error = f"Error in test_check_connection_single_thread: Connection is single threaded.\n  - Actual: {connection_is_threaded}"
        return False, error
    else:
        return True, "Connection is not single threaded."


#----------------
#-----Tests------
#----------------


def test_get_vehicle_year_by_vin(db: Database = None) -> tuple:
   

    db = Database("database/storeRecords.db") if db is None else db
    vehicle_year = db.get_vehicle_year_by_vin(1234)

    if vehicle_year != 2022:
        error = f"Error in test_get_vehicle_year_by_vin: Year is incorrect.\n  - Actual: {vehicle_year}"
        return False, error
    else:
        return True, "Test_get_vehicle_year_by_vin is CORRECT"


def test_get_vehicle_make_by_vin(db: Database = None) -> tuple:
   

    db = Database("database/storeRecords.db") if db is None else db
    vehicle_make = db.get_vehicle_make_by_vin(1234)

    if vehicle_make != "Ford":
        error = f"Error in test_get_vehicle_make_by_vin: Make is INCORRECT.\n  - Actual: {vehicle_make}"
        return False, error
    else:
        return True, "Test_get_vehicle_make_by_vin is CORRECT"

def test_get_email_by_username(db: Database = None) -> tuple:
   

    db = Database("database/storeRecords.db") if db is None else db
    user_email = db.get_email_by_username("aturing")

    if user_email != "alan@enigma.com":
        error = f"Error in test_get_email_by_username: email is incorrect.\n  - Actual: {user_email}"
        return False, error
    else:
        return True, "test_get_email_by_username is CORRECT"


def test_get_first_name_by_username(db: Database = None) -> tuple:
   

    db = Database("database/storeRecords.db") if db is None else db
    user_first_name = db.get_first_name_by_username("aturing")

    if user_first_name != "Alan":
        error = f"Error in test_get_first_name_by_username: email is incorrect.\n  - Actual: {user_first_name}"
        return False, error
    else:
        return True, "test_get_first_name_by_username is CORRECT"
