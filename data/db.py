import sqlite3
import os
import discord

def create_table(cursor):
    cursor.execute("""CREATE TABLE Messages (
    MessageID integer,
    UserID integer,
    Content text,
    GuildID integer
    )""")

def insert_user(cursor):
    cursor.execute("INSERT INTO Messages VALUES (1,1,\"Test Text\", 1)")

def mockget(cursor):
    cursor.execute("SELECT * FROM Messages")
    print(cursor.fetchall())

def save(message:discord.Message):
    path = os.getcwd() + os.sep + "data" + os.sep
    conn = sqlite3.connect(path + "Ghostie.db")
    c = conn.cursor()
    c.execute("INSERT INTO " + "Messages VALUES (?, ?, ?, ?)", (message.id, message.author.id, message.content, message.guild.id))
    conn.commit()
    conn.close()

def clean_table(cursor):
    cursor.execute("DELETE FROM Messages;")

def count_by_guild():
    conn = sqlite3.connect("Ghostie.db")
    c = conn.cursor()
    c.execute("SELECT count(*) FROM Messages GROUP BY GuildID;")
    print(c.fetchall())
    conn.close()

if __name__ == "__main__":
    #conn = sqlite3.connect("Ghostie.db")
    #c = conn.cursor()
    #create_table(c)
    #insert_user(c)
    #mockget(c)
    #clean_table(c)
    #mockget(c)
    #conn.commit()
    #conn.close()
    count_by_guild()
