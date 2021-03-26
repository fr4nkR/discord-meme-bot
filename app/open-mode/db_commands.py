import sqlite3
import datetime

DATABASE = str(os.getenv('DATABASE_NAME'))

def create_tables():
    create_meme_table()
    create_user_table()

def create_meme_table():
    """Call this function whenever we want to create the meme table inside our database"""
    #Connecting to sqlite
    conn = sqlite3.connect(DATABASE)

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Creating table as per requirement
    sql ='''CREATE TABLE IF NOT EXISTS MEME(
    link TEXT NOT NULL PRIMARY KEY,
    title TEXT,
    denied INTEGER DEFAULT 0,
    sent INTEGER DEFAULT 0,
    UNIQUE(link)
    )'''
    cursor.execute(sql)
    print("Table created successfully........")

    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()

def create_user_table():
    """Call this function whenever we want to create the user table inside our database"""
    #Connecting to sqlite
    conn = sqlite3.connect(DATABASE)

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Creating table as per requirement
    sql ='''CREATE TABLE IF NOT EXISTS USER(
    userid TEXT NOT NULL PRIMARY KEY,
    username TEXT,
    date_created datetime,
    UNIQUE(link)
    )'''
    cursor.execute(sql)
    print("Table created successfully........")

    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()

def insert_meme(link, title):
    """Call this function whenever we get a meme from reddit. We will store it in the database with
    the denied and sent values set to false"""
    try:
        meme = (link,title)
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute('INSERT OR IGNORE INTO memes VALUES (?,?)', meme)
        con.commit()
    except sqlite3.Error as error:
        print("Failed to insert data into sql table", error)
    finally:
        if con:
            con.close()
            print("sqlite connection is closed")
            
def deny_meme(link):
    """Call this function when we know that a meme is already in the database. We simply set the field
    denied equals to true"""
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        sql = ''' UPDATE memes
                    SET denied = 1
                    WHERE link = ?'''
                
        cur.execute(sql, link)
        con.commit()
    except sqlite3.Error as error:
        print("Failed update denied field on this specific meme from sql table", error)
    finally:
        if con:
            con.close()
            print("sqlite connection is closed")

def sent_meme(link):
    """Call this function when a meme is sent, regardless of weather it is approved or not, we know
    it was already sent to a user to either sending it to the meme channel or mark as inappropiate"""
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        sql = ''' UPDATE memes
                    SET sent = 1
                    WHERE link = ?'''
                
        cur.execute(sql, link)
        con.commit()
    except sqlite3.Error as error:
        print("Failed update sent field on this specific meme from sql table", error)
    finally:
        if con:
            con.close()
            print("sqlite connection is closed")

def insert_user(userid, username):
    """Call this function whenever we want to add a user to our registered users table"""
    try:
        datetime = datetime.datetime.now()
        user = (userid,username,datetime)
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute('INSERT OR IGNORE INTO users VALUES (?,?,?)', user)
        con.commit()
    except sqlite3.Error as error:
        print("Failed to insert data into sql table", error)
    finally:
        if con:
            con.close()
            print("sqlite connection is closed")      
            