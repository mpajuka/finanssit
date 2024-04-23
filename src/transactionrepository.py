from database_connection import get_database_connection


class Transaction:
    def __init__(self, name, amount) -> None:
        self.name = name
        self.amount = amount


class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all_transactions_with_profile(self, profile_name):
        cursor = self._connection.cursor()

        cursor.execute(
            "select profile_id from profiles where profile_name = ?", (profile_name,))

        row = cursor.fetchone()

        cursor.execute(
            "select * from transaction_event where profile_id = ?", (row["profile_id"],))

        rows = cursor.fetchall()

        return [Transaction(row["transaction_name"],
                            row["transaction_amount"]) for row in rows] if rows else []

    def create_transaction(self, name, amount, profile):
        cursor = self._connection.cursor()

        cursor.execute("insert into transaction_event (transaction_name," +
                       "transaction_amount, profile_id)" +
                       "values (?,?,?)",
                       (name, amount, profile.id))

        self._connection.commit()

        return profile


transaction_repository = TransactionRepository(get_database_connection())
