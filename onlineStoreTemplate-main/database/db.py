from core.utils import dict_factory, calculate_cost
import datetime as dt
import sqlite3


class Database:
    """
    A class that handles all database operations.

    args:
        - database_path: The path to the database file.

    attributes:
        - database_path: The path to the database file.
        - connection: The connection to the database.
        - cursor: The cursor of the database.
    """

    def __init__(self, database_path: str = "storeRecords.db") -> None:
        self.database_path = database_path
        self.connection = sqlite3.connect(
            database_path, check_same_thread=False)
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    # --------------------------------------------
    # ----------------- INVENTORY ----------------
    # --------------------------------------------

    def insert_new_item(self, item_name: str, price: int, info: str) -> None:
        """
        Inserts a new item_item into the database.

        args:
            - item_name: The name of the item.
            - price: The price of the item.
            - info: The info of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "INSERT INTO inventory (item_name, price, info) VALUES (?, ?, ?)", (item_name, price, info))
        self.connection.commit()

    # ------ Getter methods ------

    def get_full_inventory(self):
        """
        Gets all inventory in the database.

        args:
            - None

        returns:
            - List of the full inventory table from the database.
        """
        self.cursor.execute("SELECT * FROM inventory")
        return self.cursor.fetchall()

    def get_all_item_ids(self):
        """
        Gets all item ids in the database.

        args:
            - None

        returns:
            - List of all item ids in the database.
        """
        self.cursor.execute("SELECT id FROM inventory")
        return self.cursor.fetchall()

    def get_item_name_by_id(self, item_id: int):
        """
        Gets an item's name from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The item with the given id.
        """
        self.cursor.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    def get_item_info_by_id(self, item_id: int):
        """
        Gets the info (description) of an item from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The info of the item with the given id.
        """
        self.cursor.execute(
            "SELECT info FROM inventory WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    def get_item_price_by_id(self, item_id: int):
        """
        Gets the price of an item from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The price of the item with the given id.
        """
        self.cursor.execute(
            "SELECT price FROM inventory WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    def get_item_stock_by_id(self, item_id: int):
        """
        Gets the stock of an item from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The stock of the item with the given id.
        """
        self.cursor.execute(
            "SELECT stock FROM inventory WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    def get_item_image_url_by_id(self, item_id: int):
        """
        Gets the image_url of an item from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The image_url of the item with the given id.
        """
        self.cursor.execute(
            "SELECT image_url FROM inventory WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    def get_item_category_by_id(self, item_id: int):
        """
        Gets the category of an item from the database.

        args:
            - item_id: The id of the item to get.

        returns:
            - The category of the item with the given id.
        """
        self.cursor.execute(
            "SELECT category FROM inventory WHERE id = ?", (item_id,))
        return self.cursor.fetchone()

    # ------ Setter methods ------

    def set_item_name(self, item_id: int, new_name: str):
        """
        Updates the name of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_name: The new name of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE inventory SET name = ? WHERE id = ?", (new_name, item_id))
        self.connection.commit()

    def set_item_info(self, item_id: int, new_info: str):
        """
        Updates the information of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_info: The new information of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE inventory SET info = ? WHERE id = ?", (new_info, item_id))
        self.connection.commit()

    def set_item_price(self, item_id: int, new_price: float):
        """
        Updates the price of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_price: The new price of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE inventory SET price = ? WHERE id = ?", (new_price, item_id))
        self.connection.commit()

    def set_item_stock(self, item_id: int, new_stock: int):
        """
        Updates the stock of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_stock: The new stock of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE inventory SET stock = ? WHERE id = ?", (new_stock, item_id))
        self.connection.commit()

    def set_item_image_url(self, item_id: int, new_image_url: str):
        """
        Updates the image_url of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_image_url: The new image of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE inventory SET image_url = ? WHERE id = ?", (new_image_url, item_id))
        self.connection.commit()

    def set_item_category(self, item_id: int, new_category: str):
        """
        Updates the category of an item in the database.

        args:
            - item_id: The id of the item to update.
            - new_category: The new category of the item.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE inventory SET category = ? WHERE id = ?", (new_category, item_id))
        self.connection.commit()

    # --------------------------------------------
    # ------------------ Users -------------------
    # --------------------------------------------

    def insert_user(self, username: str, password_hash: str, email: str, first_name: str, last_name: str) -> None:
        """
        Inserts a new user into the database.

        args:
            - username: The username of the user to insert.
            - password_hash: The password_hash of the user to insert.
            - email: The email of the user to insert.

        returns:
            - None
        """
        self.cursor.execute(
            "INSERT INTO users (username, password_hash, email, first_name, last_name) VALUES (?, ?, ?, ?, ?)",
            (username, password_hash, email, first_name, last_name))
        self.connection.commit()

    # ------ Getter methods ------

    def get_all_user_information(self):
        """
        Gets all user information from the database.

        args:
            - None

        returns:
            - A list of all user information in the database.
        """
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_password_hash_by_username(self, username: str):
        """
        Gets the password hash of a user from the database.

        args:
            - username: The username of the user whose password hash to get.

        returns:
            - The password hash for the user with the given username.
        """
        self.cursor.execute(
            "SELECT password_hash FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_email_by_username(self, username: str):
        """
        Gets the email of a user from the database.

        args:
            - username: The username of the user whose email to get.

        returns:
            - The email for the user with the given username.
        """
        self.cursor.execute(
            "SELECT email FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_first_name_by_username(self, username: str):
        """
        Gets the first name of a user from the database.

        args:
            - username: The username of the user whose first name to get.

        returns:
            - The first name for the user with the given username.
        """
        self.cursor.execute(
            "SELECT first_name FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_last_name_by_username(self, username: str):
        """
        Gets the last name of a user from the database.

        args:
            - username: The username of the user whose last name to get.

        returns:
            - The last name for the user with the given username.
        """
        self.cursor.execute(
            "SELECT last_name FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    # ------ Setter methods ------

    def set_password_hash(self, username: str, new_password_hash: str):
        """
        Updates the password hash of a user in the database.

        args:
            - username: The username of the user to update.
            - new_password_hash: The new password hash of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET password_hash = ? WHERE username = ?", (new_password_hash, username))
        self.connection.commit()

    def set_email(self, username: str, new_email: str):
        """
        Updates the email of a user in the database.

        args:
            - username: The username of the user to update.
            - new_email: The new email of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET email = ? WHERE username = ?", (new_email, username))
        self.connection.commit()

    def set_first_name(self, username: str, new_first_name: str):
        """
        Updates the first name of a user in the database.

        args:
            - username: The username of the user to update.
            - new_first_name: The new first name of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET first_name = ? WHERE username = ?", (new_first_name, username))
        self.connection.commit()

    def set_last_name(self, username: str, new_last_name: str):
        """
        Updates the last name of a user in the database.

        args:
            - username: The username of the user to update.
            - new_last_name: The new last name of the user.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE users SET last_name = ? WHERE username = ?", (new_last_name, username))
        self.connection.commit()

    # --------------------------------------------
    # ------------------ Sales -------------------
    # --------------------------------------------

    def insert_new_sale(self, transaction_id: int, username: str, item_id: int, quantity: int, sale_date: dt.date, cost: float):
        """
        Inserts a new sale into the database.

        args:
            - transaction_id: The transaction id of the sale.
            - username: The username of the sale.
            - item_id: The item id of the sale.
            - quantity: The quantity of the sale.
            - sale_date: The sale date of the sale.
            - cost: The cost of the sale.

        returns:
            - None
        """
        self.cursor.execute(
            "INSERT INTO sales (transaction_id, username, item_id, quantity, sale_date, cost) VALUES (?, ?, ?, ?, ?, ?)",
            (transaction_id, username, item_id, quantity, sale_date, cost))
        self.connection.commit()

    # ------ Getter methods ------

    def get_full_sales_information(self):
        """
        Gets all sales information from the database.

        args:
            - None

        returns:
            - A list of all sales information in the database.
        """
        self.cursor.execute("SELECT * FROM sales")
        return self.cursor.fetchall()

    def get_transaction_id_by_sale_id(self, sale_id: int):
        """
        Gets the transaction id for a sale from the database.

        args:
            - sale_id: The id of the sale whose transaction id to get.

        returns:
            - The transaction id for the sale with the given id.
        """
        self.cursor.execute(
            "SELECT transaction_id FROM sales WHERE sale_id = ?", (sale_id,))
        return self.cursor.fetchone()

    def get_username_by_sale_id(self, sale_id: int):
        """
        Gets the username for a sale from the database.

        args:
            - sale_id: The id of the sale whose username to get.

        returns:
            - The username for the sale with the given id.
        """
        self.cursor.execute(
            "SELECT username FROM sales WHERE sale_id = ?", (sale_id,))
        return self.cursor.fetchone()

    def get_item_id_by_sale_id(self, sale_id: int):
        """
        Gets the item id for a sale from the database.

        args:
            - sale_id: The id of the sale whose item id to get.

        returns:
            - The item id for the sale with the given id.
        """
        self.cursor.execute(
            "SELECT item_id FROM sales WHERE sale_id = ?", (sale_id,))
        return self.cursor.fetchone()

    def get_quantity_by_sale_id(self, sale_id: int):
        """
        Gets the quantity for a sale from the database.

        args:
            - sale_id: The id of the sale whose quantity to get.

        returns:
            - The quantity for the sale with the given id.
        """
        self.cursor.execute(
            "SELECT quantity FROM sales WHERE sale_id = ?", (sale_id,))
        return self.cursor.fetchone()

    def get_sale_date_by_sale_id(self, sale_id: int):
        """
        Gets the sale date for a sale from the database.

        args:
            - sale_id: The id of the sale whose sale date to get.

        returns:
            - The sale date for the sale with the given id.
        """
        self.cursor.execute(
            "SELECT sale_date FROM sales WHERE sale_id = ?", (sale_id,))
        return self.cursor.fetchone()

    def get_cost_by_sale_id(self, sale_id: int):
        """
        Gets the cost for a sale from the database.

        args:
            - sale_id: The id of the sale whose cost to get.

        returns:
            - The cost for the sale with the given id.
        """
        self.cursor.execute(
            "SELECT cost FROM sales WHERE sale_id = ?", (sale_id,))
        return self.cursor.fetchone()

    def get_full_sale_by_id(self, sale_id: int):
        """
        Gets the sales for a sale from the database.

        args:
            - sale_id: The id of the sale whose information to get.

        returns:
            - The sales records for the sale with the given id.
        """
        self.cursor.execute(
            "SELECT * FROM sales WHERE sale_id = ?", (sale_id,))
        return self.cursor.fetchone()

    def get_sales_by_transaction_id(self, transaction_id: int):
        """
        Gets the sales for a transaction from the database.

        args:
            - transaction_id: The id of the transaction whose sales to get.

        returns:
            - The sales for the transaction with the given id.
        """
        self.cursor.execute(
            "SELECT * FROM sales WHERE transaction_id = ?", (transaction_id,))
        return self.cursor.fetchall()

    def get_sales_by_username(self, username: str):
        """
        Gets the sales for a user from the database.

        args:
            - username: The username of the user whose sales to get.

        returns:
            - The sales for the user with the given username.
        """
        self.cursor.execute(
            "SELECT * FROM sales WHERE username = ?", (username,))
        return self.cursor.fetchall()

    def get_sales_by_item_id(self, item_id: int):
        """
        Gets the sales for an item from the database.

        args:
            - item_id: The id of the item we are getting sales for.

        returns:
            - The sales for the item with the given id.
        """
        self.cursor.execute(
            "SELECT * FROM sales WHERE item_id = ?", (item_id,))
        return self.cursor.fetchall()

    def get_sales_by_date_range(self, start_date: dt.date, end_date: dt.date):
        """
        Gets the sales for a date range from the database.

        args:
            - start_date: The start date of the date range.
            - end_date: The end date of the date range.

        returns:
            - The sales for the given date range.
        """
        self.cursor.execute(
            "SELECT * FROM sales WHERE sale_date BETWEEN ? AND ?", (start_date, end_date))
        return self.cursor.fetchall()

    def get_sales_by_quantity_range(self, start_quantity: int, end_quantity: int):
        """
        Gets the sales for a quantity range from the database.

        args:
            - start_quantity: The start quantity of the quantity range.
            - end_quantity: The end quantity of the quantity range.

        returns:
            - The sales for the given quantity range.
        """
        self.cursor.execute(
            "SELECT * FROM sales WHERE quantity BETWEEN ? AND ?", (start_quantity, end_quantity))
        return self.cursor.fetchall()

    def get_sales_by_cost_range(self, start_cost: float, end_cost: float):
        """
        Gets the sales for a cost range from the database.

        args:
            - start_cost: The start cost of the cost range.
            - end_cost: The end cost of the cost range.

        returns:
            - The sales for the given cost range.
        """
        self.cursor.execute(
            "SELECT * FROM sales WHERE cost BETWEEN ? AND ?", (start_cost, end_cost))
        return self.cursor.fetchall()

    # ------ Setter methods ------

    def set_sale_transaction_id(self, sale_id: int, new_transaction_id: int):
        """
        Updates the transaction id of a sale in the database.

        args:
            - sale_id: The id of the sale to update.
            - new_transaction_id: The new transaction id of the sale.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE sales SET transaction_id = ? WHERE id = ?", (new_transaction_id, sale_id))
        self.connection.commit()

    def set_sale_username(self, sale_id: int, new_username: str):
        """
        Updates the username of a sale in the database.

        args:
            - sale_id: The id of the sale to update.
            - new_username: The new username of the sale.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE sales SET username = ? WHERE id = ?", (new_username, sale_id))
        self.connection.commit()

    def set_sale_item_id(self, sale_id: int, new_item_id: int):
        """
        Updates the item id of a sale in the database.

        args:
            - sale_id: The id of the sale to update.
            - new_item_id: The new item id of the sale.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE sales SET item_id = ? WHERE id = ?", (new_item_id, sale_id))
        self.connection.commit()

    def set_sale_date(self, sale_id: int, new_sale_date: dt.date):
        """
        Updates the sale date of a sale in the database.

        args:
            - sale_id: The id of the sale to update.
            - new_sale_date: The new sale date of the sale.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE sales SET sale_date = ? WHERE id = ?", (new_sale_date, sale_id))
        self.connection.commit()

    def set_sale_quantity(self, sale_id: int, new_quantity: int):
        """
        Updates the quantity of a sale in the database.

        args:
            - sale_id: The id of the sale to update.
            - new_quantity: The new quantity of the sale.

        returns:
            - None
        """
        self.cursor.execute(
            "UPDATE sales SET quantity = ? WHERE id = ?", (new_quantity, sale_id))
        self.connection.commit()

    def set_sale_cost(self, sale_id: int, discount: float = 0, tax: float = 0.05):
        """
        Updates the cost of a sale in the database.

        args:
            - sale_id: The id of the sale to update.

        returns:
            - None
        """
        item_id = self.get_item_id_by_sale_id(sale_id)
        quantity = self.get_quantity_by_sale_id(sale_id)
        item_price = self.get_item_price_by_id(item_id)
        new_cost = calculate_cost(item_price, quantity, discount, tax)

        self.cursor.execute(
            "UPDATE sales SET cost = ? WHERE id = ?", (new_cost, sale_id))
        self.connection.commit()
