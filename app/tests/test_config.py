""" Configuration file for testing """
class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False