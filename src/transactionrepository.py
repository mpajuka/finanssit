from database_connection import get_database_connection


class Transaction:
    def __init__(self, name, amount, profile, transaction_id=None) -> None:
        self.name = name
        self.amount = amount
        self.profile = profile
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
                            row["transaction_id"]) for row in rows] if rows else []

    def create_transaction(self, t):
        cursor = self._connection.cursor()

        cursor.execute("insert into transaction_event (transaction_name," +
                       "transaction_amount, profile_id)" +
                       "values (?,?,?)",
                       (t.name, t.amount, t.profile.id))

        self._connection.commit()

        cursor.execute("select MAX(transaction_id) as latest from transaction_event")

        row = cursor.fetchone()

        t.id = row["latest"]

        return t

    def edit_transaction(self, t):
        cursor = self._connection.cursor()

        cursor.execute("update transaction_event set transaction_name = ?, " +
                       "transaction_amount = ? where transaction_id = ?", (t.name, t.amount, t.id))

        self._connection.commit()

        return t

    def sum_of_profile_transactions(self, profile):
        cursor = self._connection.cursor()

        cursor.execute(
            "select SUM(transaction_amount) as balance from transaction_event where profile_id = ?", (profile.id,))

        row = cursor.fetchone()


        return row["balance"] if row else None

transaction_repository = TransactionRepository(get_database_connection())
