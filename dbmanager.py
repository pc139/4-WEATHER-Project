import sqlite3
import random
import hashlib
import argparse
import os

conn = None
cursor = None


def open_and_create(db_path):
    """Check the existence of a sql database or create a new one containing
    username, password, api key and salt, using username as primary key.

    Keyword arguments:
    path - Location of the database file
    """

    global conn
    global cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM users')
    except sqlite3.OperationalError:
        # if the table does not exist create one
        cursor.execute('''CREATE TABLE users
                       (username VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        api_key VARCHAR(255) NOT NULL,
                        salt SMALLINT NOT NULL,
                        PRIMARY KEY (username))''')


def create_new_user(username, password, api_key):
    """Saves in the databse the:
    - username
    - digest (the hash of password + salt)
    - api key
    - salt (random number)

    Keyword arguments:
    username – The users’ username
    password -- The  users’ password
    api_key --- The users’ personal api key
    """

    global conn
    global cursor
    user_list = display_all_users()
    if username not in user_list:
        salt = random.randint(1, 100)
        digest = str(salt) + password
        for i in range(1000000):
            digest = hashlib.sha512(digest.encode('utf-8')).hexdigest()
        # if the user already exists, replace its password and salt
        cursor.execute('INSERT OR REPLACE INTO users VALUES (?,?,?,?)',
                       (username, digest, api_key, salt))
        conn.commit()
        print ('Successfully inserted user {}'.format(username))
    else:
        print ('The username is not avaible, please choose another one!')


def remove_username(username):
    """Remove a user from the users table.

    Keyword arguments:
    username – The users’ username
    """

    global conn
    global cursor
    # the username is the primary key
    cursor.execute('DELETE FROM users WHERE username = ?', (username, ))
    conn.commit()


def check_for_username(username, password):
    """Check the presence of the user username to log-in.

    Key arguments:
    username – The users’ username
    password -- The  users’ password
    """

    global conn
    global cursor
    rows = cursor.execute('SELECT * FROM users WHERE username=?',
                          (username, ))
    conn.commit()
    results = rows.fetchall()
    # get the salt and prepend to the password before computing the digest
    digest = str(results[0][3]) + password
    for i in range(1000000):
        digest = hashlib.sha512(digest.encode('utf-8')).hexdigest()
    # if the digest in the database is equal to the computed digest ALLOW
    if digest == results[0][1].lower():
        return True
    else:
        return False


def get_api_key(username, password):
    """Find users' api key.

    Key arguments:
    username – The users’ username
    password -- The  users’ password
    """

    global conn
    global cursor
    rows = cursor.execute('SELECT * FROM users WHERE username=?',
                          (username, ))
    conn.commit()
    results = rows.fetchall()
    api_key = results[0][2]
    return api_key


def display_all_users():
    """Displays all the username for all the users.
    This function is available only for admin user.
    """

    global conn
    global cursor
    rows = cursor.execute('SELECT username FROM users')
    conn.commit()
    user_list = []
    results = rows.fetchall()
    for row in results:
        user_list += [row[0]]
    return user_list


def parse_arguments():
    """Parses all the arguments passed by the user"""

    parser = argparse.ArgumentParser(description='Manage user actions',
                                     prog='weather_info',
                                     usage='%(prog)s [options]',
                                     epilog='Using SQLite3')
    # command to add users
    parser.add_argument('-add', help='Add user', required=False,
                        default=False, action='store_true')
    # command to remove users
    parser.add_argument('-rm', help='Remove user', required=False,
                        default=False, action='store_true')
    # command to display all users
    parser.add_argument('-ds', help='Display users', required=False,
                        default=False, action='store_true')
    # user credentials
    parser.add_argument('-u', help='user username (requires -p)',
                        required=True, default=None)
    parser.add_argument('-p', help='user password', required=True,
                        default=None)
    parser.add_argument('-a', help='user api_key', required=False,
                        default=None)

    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    path = 'weather_package/data/database.db'
    open_and_create(path)
    args = parse_arguments()
    # if the users wants to add and remove a user at the same time DENY
    if args.add and args.rm:
        print ('It is not possible to add and remove a user at the same time!')
    elif args.add:
        # if there is one argument missing (username, password or both) DENY
        if args.u is None or args.p is None or args.a is None:
            print ('Something is missing, provide proper data!')
        else:
            create_new_user(args.u, args.p, args.a)
    elif args.rm:
        remove_username(args.u)
        print ('Successfully removed user {}'.format(args.u))
    elif args.ds:
        if args.u == 'admin':
            if check_for_username(args.u, args.p):
                user_list = display_all_users()
                print ("Users' list: ")
                print (user_list)
    else:
        print ('Choose -add to add or -rm to remove a user!')
