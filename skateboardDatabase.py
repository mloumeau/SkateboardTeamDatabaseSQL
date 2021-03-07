import sqlite3
from sqlite3 import Error
from datetime import datetime


def sql_connection():

    try:
        con = sqlite3.connect('skateboard.db')
        return con

    except Error:
        print(Error)


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("create table if not exists Baker(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    cursorObj.execute("create table if not exists AntiHero(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    cursorObj.execute("create table if not exists Real(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    cursorObj.execute("create table if not exists Creature(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    cursorObj.execute("create table if not exists Element(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    cursorObj.execute("create table if not exists Deathwish(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    cursorObj.execute("create table if not exists Girl(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    cursorObj.execute("create table if not exists Chocolate(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    cursorObj.execute("create table if not exists Krooked(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    cursorObj.execute("create table if not exists SantaCruz(Name text PRIMARY KEY, Age text, HomeTown text, YearTurnedPro text)")
    con.commit()


def sql_insert(con, table, entities):

    cursorObj = con.cursor()
    cursorObj.execute(f'REPLACE INTO {table}(Name, Age, HomeTown, YearTurnedPro) VALUES(?, ?, ?, ?)', entities)
    con.commit()

def sql_update(con, table, set, setValue, where, whereValue):

    cursorObj = con.cursor()
    cursorObj.execute(f'UPDATE {table} SET {set} = \"{setValue}\" where {where} = \"{whereValue}\"')
    con.commit()


def sql_fetch(con, table):

    cursorObj = con.cursor()
    cursorObj.execute(f'SELECT * FROM {table}')
    rows = cursorObj.fetchall()
    
    for row in rows:
        print(row)


con = sql_connection()



sql_table(con)

baker = [('Andrew Reynolds', 1978, 'Lakeland, FL', '2000'), 
        ('Dustin Dollin', 1980, 'Ballina, New South Whales, Australia', '1998'),
        ('Bryan Herman', 1981, 'Victorville, CA', '1999'),
        ('Justin (Figgy) Figueroa', 1991, 'Irvine, CA', '2009'),
        ('Theotis Beasley', 1991, 'Inglewood, CA', '2008'),
        ('Don (Nuge) Nguyen', 1982, 'Oklahoma City, OK', '2000'),
        ('Riley Hawk', 1992, 'Carslbad, CA', '2013'),
        ('Sammy Baca', 1988, 'Las Vegas, NV', '2005'),
        ('Kevin (Spanky) Long', 1984, 'Oak Park, CA', '2003'),
        ('Rowan Zorilla', 1995, 'Vista, CA', '2016'),
        ('Tristan (T-Funk) Funkhouser', 1997, 'Woodland Hills, CA', '2017'),
        ('Elissa Steamer', 1975, 'Fort Meyers, FL', '1995'),
        ('Kader Sylla', 2002, 'Woodland Hills, CA', '2019'),
        ('Tyson Peterson', 2000, 'Melbourne, FL', '2018'),
        ('Jacopo Carozzi', 1997, 'Milan, Italy', '2020')]



# antiHero = [('John Cardiel', 1973, 'Sacramento, CA', '1995'), 
# ('Frank Gerwer', 1974, 'Long Island, NY', ),
# ('Tony Trujillo'),
# ('Peter Hewitt'),
# ('Andy Roy'), 
# ('Chris Pfanner'), 
# ('Tony Miorana'), 
# ('Grant Taylor'), 
# ('Robbie Russo'),
# ('Daan Van Der Linden'), 
# ('Jeff Grosso'),
# ('Brian Anderson')]


for skaters in baker:
    sql_insert(con, 'Baker', skaters)

for skater in baker:
    sql_update(con, 'Baker', 'Age', datetime.today().year - skater[1], 'Name', skater[0])

sql_fetch(con,'Baker')
