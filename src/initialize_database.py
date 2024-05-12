from database_connection import get_database_connection


def drop_tables(connection):
    """_summary_

    Args:
        connection (_type_): _description_
    """    
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')
    cursor.execute('''
        drop table if exists profiles;
    ''')

    cursor.execute('''
        drop table if exists transaction_event;
    ''')

    connection.commit()


def create_tables(connection):
    """_summary_

    Args:
        connection (_type_): _description_
    """    
    cursor = connection.cursor()

    # Create users
    cursor.execute('''
        create table users (
            user_id INTEGER PRIMARY KEY,
            username text NOT NULL,
            password text NOT NULL
        );
    ''')

    # Create profiles
    cursor.execute('''
       create table profiles (
            profile_id INTEGER PRIMARY KEY,
            profile_name TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
        );
    ''')

    # Create transaction
    cursor.execute('''
        create table transaction_event (
            transaction_id INTEGER PRIMARY KEY,
            transaction_name TEXT NOT NULL,
            transaction_amount DECIMAL (65,2),
            transaction_date DATE,
            profile_id INTEGER NOT NULL,
            FOREIGN KEY (profile_id)
                REFERENCES profiles (profile_id)
        );
    ''')

    connection.commit()


def initialize_database():
    """_summary_
    """    
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
