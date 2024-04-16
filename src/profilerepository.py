from database_connection import get_database_connection

class Profile:
    def __init__(self, profile_name, profile_owner=None) -> None:
        self.name = profile_name
        self.owner = profile_owner

class ProfileRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all_with_user(self, username):
        cursor = self._connection.cursor()

        cursor.execute("select user_id from users where username = ?", (username,))

        row = cursor.fetchone()
        print(row["user_id"])

        cursor.execute("select * from profiles where user_id = ?", (row["user_id"],))

        rows = cursor.fetchall()


        return [Profile(row["profile_name"], row["user_id"]) for row in rows] if rows else []

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from profiles")

        rows = cursor.fetchall()

        return [Profile(row["profile_name"], row["user_id"]) for row in rows]

    def find_profile(self, profile_name):
        cursor = self._connection.cursor()

        cursor.execute("select * from profiles where profile_name = ?", (profile_name,))

        row = cursor.fetchone()

        return Profile(row["profile_name"], row["user_id"]) if row else None

    def create_new_profile(self, profile):
        cursor = self._connection.cursor()

        cursor.execute("insert into profiles (profile_name, user_id) values (?,?)",
                       (profile.name, profile.owner))

        self._connection.commit()

        return profile


profile_repository = ProfileRepository(get_database_connection())
profiles = profile_repository.find_all()
