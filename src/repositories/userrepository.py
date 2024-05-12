from database_connection import get_database_connection


class User:
    """User-class, which stores a username, password-pair for identification
    """

    def __init__(self, username: str, password: str) -> None:
        """User with username and password credentials

        Args:
            username (str): the user input username
            password (str): the user input password
        """
        self.username = username
        self.password = password


class UserRepository:
    """Class for handling user related database operations prompted from the user interface
    """

    def __init__(self, connection) -> None:
        """Initializes the repository to handle database operations

        Args:
            connection (Connection): sqlite database connection
        """
        self._connection = connection

    def find_username(self, username: str) -> User | None:
        """Returns the user object if found, based on the username
        searched

        Args:
            username (str): the username to be searched

        Returns:
            User | None: returns the user if found
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from users where username = ?", (username,))

        row = cursor.fetchone()

        return User(row["username"], row["password"]) if row else None

    def create_new_user(self, user: User) -> User:
        """Creates a new user based on the existing object

        Args:
            user (User): the user object with credential information

        Returns:
            User: the user added 
        """
        cursor = self._connection.cursor()

        cursor.execute("insert into users (username, password) values (?,?)",
                       (user.username, user.password))

        self._connection.commit()

        return user


user_repository = UserRepository(get_database_connection())
