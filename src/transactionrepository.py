from database_connection import get_database_connection


class Transaction:
    def __init__(self, name, amount, profile, date, transaction_id=None) -> None:
        self.name = name
        self.amount = amount
        self.profile = profile
        self.date = date
        self.id = transaction_id


class TransactionRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all_transactions_with_profile(self, profile):
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from transaction_event where profile_id = ?", (profile.id,))

        rows = cursor.fetchall()

        return [Transaction(row["transaction_name"],
                            row["transaction_amount"],
                            row["profile_id"],
                            row["transaction_date"],
                            row["transaction_id"]) for row in rows] if rows else []

    def create_transaction(self, t):
        cursor = self._connection.cursor()

        cursor.execute("insert into transaction_event (transaction_name," +
                       "transaction_amount, transaction_date, profile_id)" +
                       "values (?,?,?,?)",
                       (t.name, t.amount, t.date, t.profile.id))

        self._connection.commit()

        cursor.execute(
            "select MAX(transaction_id) as latest from transaction_event")

        row = cursor.fetchone()

        t.id = row["latest"]

        return t

    def edit_transaction(self, t):
        cursor = self._connection.cursor()

        cursor.execute("update transaction_event set transaction_name = ?, " +
                       "transaction_amount = ?, transaction_date = ? where transaction_id = ?",
                       (t.name, t.amount, t.date, t.id))

        self._connection.commit()

        return t

    def remove_transaction(self, transaction_id):
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from transaction_event where transaction_id = ?", (transaction_id,))
        self._connection.commit()

        return True

    def sum_of_profile_transactions(self, profile):
        cursor = self._connection.cursor()

        cursor.execute(
            "select SUM(transaction_amount) as balance from transaction_event where profile_id = ?",
            (profile.id,))

        row = cursor.fetchone()

        return row["balance"] if row else None

    def get_transaction(self, transaction_id):
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from transaction_event where transaction_id = ?", (
                transaction_id,)
        )

        row = cursor.fetchone()

        return Transaction(row["transaction_name"],
                           row["transaction_amount"],
                           row["profile_id"],
                           row["transaction_date"],
                           row["transaction_id"]) if row else None


transaction_repository = TransactionRepository(get_database_connection())
