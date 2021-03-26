import sqlite3
import time

DATABASE_MEMES = str(os.getenv('DATABASE_NAME'))
DATABASE_USERS = str(os.getenv('DATABASE_USERS'))

def insert_meme(link, title):
    """Call this function whenever we get a meme from reddit. We will store it in the database with
    the denied and sent values set to false"""
    try:
        meme = (link,title)
        con = sqlite3.connect(DATABASE_MEMES)
        cur = con.cursor()
        cur.execute('INSERT INTO memes VALUES (?,?)', meme)
        con.commit()
    except sqlite3.Error as error:
        print("Failed to insert data into sql table", error)
    finally:
        if con:
            con.close()
            print("sqlite connection is closed")
            
def deny_meme(title):
    """Call this function when we know that a meme is already in the database. We simply set the field
    denied equals to true"""
    try:
        meme = (link,title)
        con = sqlite3.connect(DATABASE_MEMES)
        cur = con.cursor()
        sql = ''' UPDATE memes
                    SET denied = 1
                    WHERE link = ?'''
                
        cur.execute(sql, title)
        con.commit()
    except sqlite3.Error as error:
        print("Failed update denied field on this specific meme from sql table", error)
    finally:
        if con:
            con.close()
            print("sqlite connection is closed")

def sent_meme(title):
    """Call this function when a meme is sent, regardless of weather it is approved or not, we know
    it was already sent to a user to either sending it to the meme channel or mark as inappropiate"""
    try:
        meme = (link,title)
        con = sqlite3.connect(DATABASE_MEMES)
        cur = con.cursor()
        sql = ''' UPDATE memes
                    SET sent = 1
                    WHERE link = ?'''
                
        cur.execute(sql, title)
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
        datetime = time.time()
        user = (userid,username,datetime)
        con = sqlite3.connect(DATABASE_USERS)
        cur = con.cursor()
        cur.execute('INSERT INTO users VALUES (?,?,?)', user)
        con.commit()
    except sqlite3.Error as error:
        print("Failed to insert data into sql table", error)
    finally:
        if con:
            con.close()
            print("sqlite connection is closed")      
            