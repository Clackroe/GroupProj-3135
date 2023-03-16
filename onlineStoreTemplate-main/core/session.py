from core.utils import calculate_total_cost
from datetime import datetime
from database.db import Database


class UserSession:
    """
    UserSession is a class that represents a user's shopping session.

    args:
        - username: The username of the user.
        - db: The database to use.

    attributes:
        - username: The username of the user.
        - cart: A dictionary of dictionaries representing the items in the user's cart.
        - total_cost: The total cost of the user's cart.
        - date: The date of the user's session.
        - db: The database to use.
    """

    def __init__(self, username: str, db: Database):
        self.username = username
        self.total_cost = 0
        self.date = None
        self.db = db
        self.cart = self.empty_cart()

    def empty_cart(self) -> dict:
        """
        Fills the cart dictionary with item ids and 0 quantities.

        args:
            - None

        returns:
            - A dictionary of dictionaries representing the items in the user's cart.
        """
        inventory = self.db.get_full_inventory()
        new_cart = {}
        for item in inventory:
            new_cart[item["id"]] = {"name": item["item_name"], "price": item["price"], "quantity": 0,
                                    "discount": 0, "tax_rate": 0}
        return new_cart

    def is_item_in_cart(self, id: str) -> bool:
        """
        Checks if an item is in the user's cart.

        args:
            - id: The id of the item.

        returns:
            - True if the item is in the user's cart, False otherwise.
        """
        return id in self.cart

    def add_new_item(self, id: str, name: str, price: int, quantity: int, discount: float = 0.0, tax_rate: float = 0.05) -> None:
        """
        Creates a new item to add to the user's cart.

        args:
            - id: The id of the item.
            - name: The name of the item.
            - price: The price of the item.
            - quantity: The quantity of the item.
            - discount: The discount of the item.
            - tax_rate: The tax rate of the item.

        returns:
            - None
        """
        self.cart[id] = {"name": name, "price": price, "quantity": quantity,
                         "discount": discount, "tax_rate": tax_rate}

    def update_item_quantity(self, id: str, change_to_quantity: int) -> None:
        """
        Updates the quantity of an item in the user's cart.

        args:
            - id: The id of the item.
            - quantity: The quantity of the item.
        """
        if self.cart[id]["quantity"] + change_to_quantity <= 0:
            self.remove_item(id)
        else:
            self.cart[id]["quantity"] += change_to_quantity

    def remove_item(self, id: str) -> None:
        """
        Removes an item from the user's cart.

        args:
            - id: The id of the item.
        """
        del self.cart[id]

    def update_total_cost(self) -> None:
        """
        Updates the total cost of the user's cart.
        """
        self.total_cost = calculate_total_cost(self.cart)

    def submit_cart(self) -> None:
        """
        Called when the order is submitted. Finalizes user session details.

        args:
            - None

        returns:
            - None
        """
        self.update_total_cost()
        self.date = datetime.now()


class Sessions:
    """
    Sessions is a class that represents the collection of active sessions.

    args:
        - None

    attributes:
        - sessions: A dictionary of user sessions.
    """

    def __init__(self):
        self.sessions = {}

    def add_new_session(self, username: str, db: Database) -> None:
        """
        Adds a new user session to the collection of sessions.

        args:
            - username: The username of the user.
            - db: The database to use.

        returns:
            - None
        """
        self.sessions[username] = UserSession(username, db)

    def get_session(self, username: str) -> UserSession:
        """
        Gets a user session from the collection of sessions.

        args:
            - username: The username of the user.

        returns:
            - The user session.
        """
        return self.sessions[username]

    def remove_session(self, username: str) -> None:
        """
        Removes a user session from the collection of sessions.

        args:
            - username: The username of the user.

        returns:
            - None
        """
        del self.sessions[username]

    def get_all_sessions(self) -> dict:
        """
        Gets all user sessions from the collection of sessions.

        args:
            - None

        returns:
            - A dictionary of user sessions.
        """
        return self.sessions
