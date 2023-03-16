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
