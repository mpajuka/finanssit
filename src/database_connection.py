import sqlite3
from config import DB

connection = sqlite3.connect(DB)
connection.row_factory = sqlite3.Row


def get_database_connection() -> sqlite3.Connection:
    """returns the sqlite database connection address variable

    Returns:
        sqlite3.Connection: database connection
    """
    return connection
