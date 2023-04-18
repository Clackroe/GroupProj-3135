import sys
sys.path.append('../')

from datetime import datetime
import unittest
from unittest.mock import MagicMock

from database.db import Database
from core.session import UserSession, Sessions


class TestUserSession(unittest.TestCase):

    def setUp(self):
        self.username = "test_user"
        self.db = MagicMock(spec=Database)
        self.session = UserSession(self.username, self.db)

    def test_empty_cart(self):
        self.assertEqual(len(self.session.cart), len(self.db.get_full_inventory()))

    def test_add_new_item(self):
        item_id = "item_1"
        item_name = "Test Item"
        item_price = 10
        item_quantity = 1
        self.session.add_new_item(item_id, item_name, item_price, item_quantity)
        self.assertIn(item_id, self.session.cart)
        self.assertEqual(self.session.cart[item_id]["name"], item_name)
        self.assertEqual(self.session.cart[item_id]["price"], item_price)
        self.assertEqual(self.session.cart[item_id]["quantity"], item_quantity)

    def test_update_item_quantity_add(self):
        item_id = "item_1"
        item_quantity = 1
        self.session.update_item_quantity(item_id, item_quantity)
        self.assertEqual(self.session.cart[item_id]["quantity"], item_quantity)

    def test_update_item_quantity_remove(self):
        item_id = "item_1"
        item_quantity = -1
        self.session.update_item_quantity(item_id, item_quantity)
        self.assertNotIn(item_id, self.session.cart)

    def test_remove_item(self):
        item_id = "item_1"
        self.session.remove_item(item_id)
        self.assertNotIn(item_id, self.session.cart)

    def test_update_total_cost(self):
        self.session.cart = {
            "item_1": {"name": "Test Item 1", "price": 10, "quantity": 1, "discount": 0, "tax_rate": 0.05},
            "item_2": {"name": "Test Item 2", "price": 20, "quantity": 2, "discount": 0, "tax_rate": 0.1},
            "item_3": {"name": "Test Item 3", "price": 30, "quantity": 3, "discount": 0.2, "tax_rate": 0.15}
        }
        expected_total_cost = (10 + 20*2 + 30*3*0.8) * (1 + 0.05 + 0.1 + 0.15)
        self.session.update_total_cost()
        self.assertEqual(self.session.total_cost, expected_total_cost)

    def test_submit_cart(self):
        self.session.submit_cart()
        self.assertIsNotNone(self.session.date)


class TestSessions(unittest.TestCase):

    def setUp(self):
        self.sessions = Sessions()

    def test_add_new_session(self):
        username = "test_user"
        db = MagicMock(spec=Database)
        self.sessions.add_new_session(username, db)
        self.assertIn(username, self.sessions.sessions)

    def test_get_session(self):
        username = "test_user"
        db = MagicMock(spec=Database)
        self.sessions.sessions[username] = MagicMock(spec=UserSession)
        session = self.sessions.get_session(username)
        self.assertIsInstance(session, UserSession)

    def test_remove_session(self):
        username = "test_user"
        db = MagicMock(spec=Database)
        self.sessions.sessions[username] = MagicMock(spec=UserSession)
        self.sessions.remove_session(username)
        self.assertNotIn(username, self.sessions.sessions)

    def test_get_all_sessions(self):
        username_1 = "test_user_1"
