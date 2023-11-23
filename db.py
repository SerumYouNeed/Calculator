import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                id integer PRIMARY KEY,
                                username text NOT NULL,
                                password text NOT NULL,
                                score integer,
                                score_adding integer,
                                score_subtracting integer,
                                score_muliplying ineger,
                                score_dividing integer,
                                score_quiz integer,
                                score_chalenge integer 
                            ); """

def login_avb(conn, name):
    """
    Check if creating login is unique
    :param conn:
    :param name:
    :return: True if unique
    """
    sql = ''' SELECT "username" FROM users WHERE "username"=? '''
    cur = conn.cursor()
    cur.execute(sql, name)
    conn.commit()
    user = cur.fetchone()
    if user:
        return False

def create_user(conn, user):
    """
    Create a new user in users table
    :param conn:
    :param user:
    :return: user id
    """
    sql = ''' INSERT INTO users(username,password,score)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def log_user(conn, user):
    """
    Login user into the users table
    :param conn:
    :param user:
    :return: True if success
    """
    sql = ''' SELECT * FROM users WHERE "username"=? AND "password"=? '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    row = cur.fetchone()
    if row:
        return True
    
def update_score(conn, player):
    """
    Update user's score in users table
    :param conn:
    :param player:
    """
    sql = ''' UPDATE "users" SET "score"=?
              WHERE "username"=?
          '''
    cur = conn.cursor()
    cur.execute(sql, player)
    conn.commit()

def print_scores(conn):
    sql = ''' SELECT "username", "score" FROM "users" ORDER BY "score" DESC LIMIT 10 '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    rows = cur.fetchall()
    if rows:
        return rows
    
def get_score(conn, name):
    """
    Get user's score from users table
    :param conn:
    :param name:
    """
    sql = ''' SELECT "score" FROM "users" WHERE "username"=?
          '''
    cur = conn.cursor()
    cur.execute(sql, name)
    conn.commit()
    score = cur.fetchone()
    if score:
        return score