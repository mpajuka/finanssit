from repositories.profilerepository import Profile
from database_connection import get_database_connection


class Transaction:
    """Transaction bound to a profile, storing information about 
    the name, amount, profile, date and identifier of each transaction

    Attributes:
        name (str): name of the transaction
        amount (float): incurred amount of the transaction
        profile (Profile): the Profile in which the transaction belongs
        date (str): date value in "yyyy-mm-dd" format
        id (int): transaction identifier
    """

    def __init__(self, name: str, amount: float, profile: Profile, date: str,
                 transaction_id: int = None) -> None:
        """Initializes the transaction object

        Args:
            name (str): name of user input transaction
            amount (float): amount of user input transaction
            profile (Profile): profile object in which the transaction belongs
            date (str): date value "yyyy-mm-dd" in string format 
            transaction_id (int, optional): 
                transaction identifier, empty before database insert. Defaults to None.
        """
        self.name = name
        self.amount = amount
        self.profile = profile
        self.date = date
        self.id = transaction_id


class TransactionRepository:
    """Class for handling transaction related database operations prompted from the user interface
    """

    def __init__(self, connection) -> None:
        """Initializes the repository to handle database operations

        Args:
            connection (Connection): sqlite database connection
        """
        self._connection = connection

    def find_all_transactions_with_profile(self, profile: Profile) -> list[Transaction] | list:
        """Returns all the transactions added to a specific profile

        Args:
            profile (Profile): the profile object for the transactions 

        Returns:
            list[Transaction] | list: a list of transactions if found, else an empty list
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from transaction_event where profile_id = ?", (profile.id,))

        rows = cursor.fetchall()

        return [Transaction(row["transaction_name"],
                            row["transaction_amount"],
                            row["profile_id"],
                            row["transaction_date"],
                            row["transaction_id"]) for row in rows] if rows else []

    def create_transaction(self, t: Transaction) -> Transaction:
        """Inserts the transaction to the database, and modifies
        the existing transaction objects identifier to match the
        new insert

        Args:
            t (Transaction): transaction to be added and modified

        Returns:
            Transaction: final modified transaction
        """
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

    def edit_transaction(self, t: Transaction) -> Transaction:
        """Updates the transactions data based on the users new inputs
        and the existing identfier of the transaction, which the user
        selected

        Args:
            t (Transaction): transaction to be edited

        Returns:
            Transaction: final edited transaction
        """
        cursor = self._connection.cursor()

        cursor.execute("update transaction_event set transaction_name = ?, " +
                       "transaction_amount = ?, transaction_date = ? where transaction_id = ?",
                       (t.name, t.amount, t.date, t.id))

        self._connection.commit()

        return t

    def remove_transaction(self, transaction_id: int) -> bool | None:
        """Removes the transaction from the database with the
        identifier provided

        Args:
            transaction_id (int): user selected transactions identifier

        Returns:
            True | None: returns true if the removal succeeded
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from transaction_event where transaction_id = ?", (transaction_id,))
        self._connection.commit()

        return True

    def sum_of_profile_transactions(self, profile: Profile) -> int | None:
        """Returns the sum of the transaction amount column of the
        selected profile

        Args:
            profile (Profile): profile of the transactions to be counted

        Returns:
            int | None: sum of transactions if any exist
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select SUM(transaction_amount) as balance from transaction_event where profile_id = ?",
            (profile.id,))

        row = cursor.fetchone()

        return row["balance"] if row else None

    def get_transaction(self, transaction_id: int) -> Transaction | None:
        """Returns the transaction based on the identifier

        Args:
            transaction_id (int): transaction identifier to be fetched

        Returns:
            Transaction | None: returns the transaction found, if existed
        """
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
