""" Contains tests for database functionality """
import unittest

from app.models.assets import Assets
from app.models.branch import Branch
from app.models.company import Company
from app.models.footprint import Footprint
from app.models.inventory import Inventory
from app.models.order_details import Order_details
from app.models.order import Order
from app.models.role import Role
from app.models.supplier import Supplier
from app.models.user import User
from app.models.user_to_branch import User_to_branch
from app.tests.test_config import TestConfig

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class TestDatabaseStorage(unittest.TestCase):
    """ Tests to verify database functionality """
    @classmethod
    def setUpClass(cls):
        """ Creates a testing database """
        cls.app = Flask(__name__)
        cls.app.config.from_object(TestConfig)
        cls.client = cls.app.test_client()
        cls.db = SQLAlchemy(cls.app)
        
        with cls.app.app_context():
            cls.db.create_all()


    @classmethod
    def tearDownClass(cls):
        """ Tears down existing database """
        with cls.app.app_context():
            cls.db.session.remove()
            cls.db.drop_all()


    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.db.create_all()


    def tearDown(self):
        self.db.session.rollback()
        self.db.session.remove()
        self.app_context.pop()

    def testCreateUser(self):
        """ Tests if created user exists in database. """
        company = Company(name="Test Company", RFC="RFC123", fiscal_address="Test St")
        self.db.session.add(company)
        self.db.session.commit()

        user = User(name="Test User", email="test@example.com", password="password", company_id=company.company_id)
        self.db.session.add(user)
        self.db.session.commit()
        
        retrieved_user = User.query.filter_by(email="test@example.com").first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.name, "Test User")
        self.assertEqual(retrieved_user.company.name, "Test Company")


if __name__ == '__main__':
    unittest.main()