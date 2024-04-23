from database_connection import get_database_connection


def drop_tables(connection):
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
            profile_id INTEGER NOT NULL,
            FOREIGN KEY (profile_id)
                REFERENCES profiles (profile_id)
        );
    ''')

    # test profile
    cursor.execute('''
        insert into profiles (profile_name, user_id) values ("Testiprofiili", 1);
        
    ''')

    cursor.execute('''
        insert into transaction_event (transaction_name, transaction_amount,
        profile_id) values ("Vuokra", -293.22, 1);       
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
