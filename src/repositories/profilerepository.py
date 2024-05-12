from database_connection import get_database_connection


class Profile:
    """User-bound profile, needed for storing transactions and other information

    Attributes:
        name (str): the name of the profile
        username (str): the username of the profile owner
        id (int): the profile owners identifier 
    """

    def __init__(self, profile_name: str, username: str, user_id=None) -> None:
        """_summary_

        Args:
            profile_name (str): profile name from the users input
            username (str): username value from the session
            user_id (int, optional): 
                profile owner identifier, later added along database insert.
                Defaults to None.
        """
        self.name = profile_name
        self.username = username
        self.id = user_id


class ProfileRepository:
    """Class for handling profile related database operations prompted from the user interface
    """

    def __init__(self, connection) -> None:
        """Initializes the repository to handle database operations

        Args:
            connection (Connection): sqlite database connection
        """
        self._connection = connection

    def find_all_with_user(self, username: str) -> list[Profile] | list:
        """Returns all the profiles created in the name of the user

        Args:
            username (str): the owner of the profiles

        Returns:
            list[Profile] | list: returns a list of profiles if found, else an empty list
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select user_id from users where username = ?", (username,))

        row = cursor.fetchone()

        cursor.execute(
            "select * from profiles where user_id = ?", (row["user_id"],))

        rows = cursor.fetchall()

        return [Profile(row["profile_name"],
                        row["user_id"]) for row in rows] if rows else []

    def find_profile(self, profile_name: str) -> Profile | None:
        """Returns a profile if found, based on the searched name

        Args:
            profile_name (str): name of the profile searched

        Returns:
            Profile | None: a profile if found, else None
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from profiles where profile_name = ?", (profile_name,))

        row = cursor.fetchone()

        profile_name = row["profile_name"]
        profile_id = row["profile_id"]

        cursor.execute(
            "select username from users where user_id = ?", (row["user_id"],))

        row = cursor.fetchone()

        username = row["username"]

        return Profile(profile_name, username, profile_id) if row else None

    def create_new_profile(self, profile: Profile) -> Profile:
        """Inserts the profile in the database, and adds the owners identifier
        to the object parameter

        Args:
            profile (Profile): the partial profile

        Returns:
            Profile: the profile in the parameter with updated owner identifier
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from profiles where profile_name = ?", (profile.name,))

        profile_exists = cursor.fetchone()
        if profile_exists:
            return "Error: profile name must be unique"

        cursor.execute(
            "select user_id from users where username = ?", (profile.username,))

        row = cursor.fetchone()
        profile.id = row["user_id"]

        cursor.execute("insert into profiles (profile_name, user_id) values (?,?)",
                       (profile.name, row["user_id"],))

        self._connection.commit()

        return profile


profile_repository = ProfileRepository(get_database_connection())
