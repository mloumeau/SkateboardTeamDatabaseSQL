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
    cursorObj.execute("create table if not exists Almost(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists April(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists AntiHero(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Baker(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Birdhouse(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Blind(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists BloodWizard(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Chocolate(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Creature(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Deathwish(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Element(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Enjoi(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists FA(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Flip(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Foundation(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Girl(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Habitat(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Heroin(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Madness(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Krooked(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Pizza(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists PlanB(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Primitive(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Real(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists SantaCruz(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Sk8Mafia(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists ToyMachine(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Welcome(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")
    cursorObj.execute("create table if not exists Zero(Name text PRIMARY KEY, Age text, HomeTown text, stance text)")

    con.commit()


def sql_insert(con, table, entities):

    cursorObj = con.cursor()
    cursorObj.execute(f'REPLACE INTO {table}(Name, Age, HomeTown, stance) VALUES(?, ?, ?, ?)', entities)
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


almost = []


april =    [('Shane ONeill', 1990, 'Melbourne, Australia', 'Goofy'),
            ('Yuto Horigome', 1999, 'Tokyo, Japan', 'Regular')]


antiHero = [('John Cardiel', 1973, 'Sacramento, CA', 'Goofy'), 
            ('Frank Gerwer', 1974, 'Long Island, NY', 'Regular'),
            ('Tony Trujillo', 1982, 'Santa Rosa, CA', 'Regular'),
            ('Peter Hewitt', 1973, 'San Diego, CA', 'Regular'),
            ('Andy Roy', 1976, 'Santa Cruz, CA', 'Regular'), 
            ('Chris Pfanner', 1985, 'Kennelbach, Australia', 'Goofy'), 
            ('Tony Miorana', 1980, 'N/A', 'Regular'), 
            ('Grant Taylor', 1991, 'Atlanta, GA', 'Goofy'), 
            ('Robbie Russo', 1993, 'San Pedro, CA', 'Regular'),
            ('Daan Van Der Linden', 1996, 'Eindhoven, Netherlands', 'Goofy'), 
            ('Jeff Grosso', 1968, 'Arcadia, CA', 'Goofy'),
            ('Brian Anderson', 1976, 'Groton, CT', 'Regular')]


baker =    [('Andrew Reynolds', 1978, 'Lakeland, FL', 'Regular'), 
            ('Dustin Dollin', 1980, 'Ballina, New South Whales, Australia', 'Goofy'),
            ('Bryan Herman', 1981, 'Victorville, CA', 'Regular'),
            ('Justin (Figgy) Figueroa', 1991, 'Irvine, CA', 'Goofy'),
            ('Theotis Beasley', 1991, 'Inglewood, CA', 'Goofy'),
            ('Don (Nuge) Nguyen', 1982, 'Oklahoma City, OK', 'Goofy'),
            ('Riley Hawk', 1992, 'Carslbad, CA', 'Goofy'),
            ('Sammy Baca', 1988, 'Las Vegas, NV', 'Regular'),
            ('Kevin (Spanky) Long', 1984, 'Oak Park, CA', 'Goofy'),
            ('Rowan Zorilla', 1995, 'Vista, CA', 'Goofy'),
            ('Tristan (T-Funk) Funkhouser', 1997, 'Woodland Hills, CA', 'Regular'),
            ('Elissa Steamer', 1975, 'Fort Meyers, FL', 'Regular'),
            ('Kader Sylla', 2002, 'Woodland Hills, CA', 'Goofy'),
            ('Tyson Peterson', 2000, 'Melbourne, FL', 'Goofy'),
            ('Jacopo Carozzi', 1997, 'Milan, Italy', 'Regular')]

 
birdhouse =[('Tony Hawk', 1969, 'Carlsbad, CA', 'Goofy'),
            ('Aaron (Jaws) Homoki', 1990, 'Phoenix, AZ', 'Regular'),
            ('Ben Raybourn', 1993, 'Houston, TX', 'Goofy'),
            ('Clint Walker', 1991, 'Altus, OK', 'Regular'),
            ('David Loy', 1992, 'Santa Ana, CA','Regular'),
            ('Lizzie Armanto', 1993, 'Santa Monica, CA', 'Regular'),
            ('Clive Dixon', 1993, 'Cocoa Beach, FL', 'Regular'),
            ('Shawn Hale', 1988, 'Joplin, MO', 'Goofy'),
            ('Elliot Sloan', 1989, 'New York, NY', 'Goofy')]


blind =    [('Jordan Maxham', 1991, 'Barre, VT', 'Goofy'),
            ('TJ Rogers', 1992, 'Ontario, Canada', 'Regular'),
            ('Cody McEntire', 1988, 'Belton, TX', 'Regular'),
            ('Kevin Romar', 1989, 'Cypress, CA', 'Goofy'),
            ('Micky Papa', 1991, 'Vancouver B.C., Canada', 'Regular'),
            ('Nassim Lachlab', 1997, 'Rabat Maroc, Morocco', 'Goofy'),
            ('Sora Shirai', 2002, 'Kanagawa, Japan', 'Goofy'),
            ('Jason Thurtle', 1997, 'Las Vegas, NV', 'Goofy')]


bloodWizard=[('Chris Gregson', 1991, 'Irvine, CA', 'Goofy'),
            ('Jackson Given', 1991, 'Walnut Creek', 'Regular'),
            ('Anakin, Senn', 1995, 'Grass Valley, CA', 'Regular'),
            ('Marisa Dal Santo', 1989, 'La Grange, IL', 'Regular'),
            ('Nolan Miskell', 1999, 'Riverside, CA', 'Goofy'),
            ('Shea Cooper', 1993, 'Boise, ID', 'Regular'),
            ('Kevin Kowalski', 1993, 'Portland, OR', 'Regular'),
            ('Tristan Rennie', 1999, 'Rialto, CA', 'Regular')]


chocolate =[('Vincent Alvarez', 1989, 'West Covina, CA', 'Regular'),
            ('Kenny Anderson', 1976, 'Redlands CA', 'Goofy'),
            ('Yonnie Cruz', 1988, 'Tampa, FL', 'Goofy'),
            ('Justin Eldridge', 1984, 'Los Angeles, CA', 'Goofy'),
            ('Jesus Fernandez', 1979, 'Barcelona, Spain', 'Regular'),
            ('Stevie Perez', 1991, 'North Hollywood, CA', 'Goofy'),
            ('Chris Roberts', 1978, 'Malibu, CA', 'Regular'),
            ('Raven Tershy', 1992, 'Santa Cruz, CA', 'Regular'),
            ('James Capps', 1990, 'San Francisco, CA', 'Regular'),
            ('Carl Aikens', 1999, 'Chicago, IL', 'Regular'),
            ('Erik Herrera', 1998, 'Los Angeles, CA', 'Goofy')]


creature = [('Al Partanen', 1972, 'Milwaukee, WI', 'Regular'),
            ('Darren Navarrette', 1974, 'San Diego', 'Regular'),
            ('Sam Hitz', 1973, 'N/A', 'Regular'),
            ('Stu Graham', 1983, 'Livingston, Scotland', 'Goofy'),
            ('Chris (Muscle) Russell', 1996, 'Hermosa Beach, CA', 'Goofy'),
            ('Cody Lockwood', 1997, 'Portland, OR', 'Goofy'),
            ('David Gravette', 1988, 'Issaquaa, WA', 'Goofy'),
            ('Jimmy Wilkins', 1993, 'Colombus OH', 'Regular'),
            ('Kevin Baekkel', 1996, 'Hamar, Norway', 'Regular'),
            ('Milton Martinez', 1991, 'Mar del Plata, Argentina', 'Goofy'),
            ('Willis Kimbel', 1988, 'Oceanside, CA', 'Regular')]


deathWish =[('Erik Ellington', 1977, 'Los Angeles, CA', 'Goofy'),
            ('Jim Greco', 1977, 'Los Angeles, CA', 'Regular'),
            ('Brian (Slash) Hansen', 1987, 'Vista, CA', 'Regular'),
            ('Jon Dickson', 1990, 'Antioch, IL', 'Goofy'),
            ('Mike (Lizard King) Plumb', 1985, 'Salt Lake City, UT', 'Goofy'),
            ('Neen Williams', 1985, 'Chicago, IL', 'Goofy'),
            ('Taylor Kirby', 1993, 'San Clemente, CA', 'Regular'),
            ('Jake Hayes', 1992, 'Sydney, Australia', 'Regular'),
            ('Jamie Foy', 1996, 'Deerfield Beach, FL', 'Regular')]


element =  [('Brandon Westgate', 1989, 'Wareham, MA', 'Goofy'),
            ('Ethan Loy', 1996, 'Santa Ana, CA', 'Regular'),
            ('Jaako Ojanen', 1995, 'Helsinki, Finland', 'Goofy'),
            ('Madars Apse', 1989, 'Ventspils, Latvia', 'Regular'),
            ('Mark Appleyard', 1983, 'Ontario, Canada', 'Goofy'),
            ('Nick Garcia', 1990, 'Buena Park, CA', 'Regular'),
            ('Phil Zwijsen', 1987, 'Antwerp, Belgium', 'Goofy'),
            ('Sascha Daley', 1987, 'Vancouverm Canada', 'Regular'),
            ('Tom Schaar', 2000, 'Malibu, CA', 'Regular')]


enjoi =    [('Ben Raemers', 1991, 'Walton-on-naze, United Kingdom', 'Regular'),
            ('Caswell Berry', 1987, 'San Jose, CA', 'Goofy'),
            ('Didrik (Deedz) Galasso', 1995, 'Larvik, Norway', 'Regular'),
            ('Jackson Pilz', 1992, 'Sunishine Coast Australia', 'Goofy'),
            ('Louie Barletta', 1979, 'Modesto, CA', 'Goofy'),
            ('Nestor Judkins', 1988, 'Los Gatos, CA', 'Regular'),
            ('Samarria Brevard', 1994, 'Riverside, CA', 'Goofy'),
            ('Thaynan Costa', 1995, 'Lisbon, Portufal', 'Regular'),
            ('Zack Wallin', 1989, 'San Jose, CA', 'Goofy')]


FA =       [('Jason Dill', 1977, 'Los Angeles, CA', 'Regular'),
            ('Anthony Van Engelen', 1979, 'Los Angeles, CA', 'Regular'),
            ('Na-Kel Smith', 1995, 'Los Angeles, CA', 'Regular'),
            ('Kevin Bradley', 1996, 'Los Angeles, CA', 'Goofy'),
            ('Gino Iannucci', 1982, 'Los Angeles, CA', 'Goofy'),
            ('Kevin Terpening', 1988, 'Canton, OH', 'Goofy'),
            ('Tyshawn Jones', 1999, 'Bronx, NY', 'Regular'),
            ('Sage Elsesser', 1997, 'Los Angeles, CA', 'Regular'),
            ('Sean Pablo', 1998, 'Los Angeles, CA', 'Regular'),
            ('Elijah Berle', 1995, 'Santa Monica, CA', 'Goofy'),
            ('Aidan Mackey', 1990, 'Los Angeles, CA', 'Regular'),
            ('Louie Lopez', 1995, 'Hawthorne, CA', 'Regular'),
            ('Vincent Touzery', 1990, 'Paris, France', 'Regular')]


flip = []


foundation=[('Nick Merlino', 1988, 'Atlantic City, NJ', 'Regular'),
            ('Dakota Servold', 1993, 'Phoenix, AZ', 'Goofy'),
            ('Joey Ragali', 1990, 'Jupiter, FL', 'Regular'),
            ('Ryan Spencer', 1990, 'Kihei, HI', 'Regular'),
            ('Corey Glick', 1997, 'Chicago, IL', 'Goofy'),
            ('Aidan Campbell', 1994, 'Santa Margarita, CA', 'Goofy'),
            ('Cole Wilson', 1990, 'Louisville, KY', 'Regular')]


girl =     [('Sean Malto', 1990, 'Kansas City, KS', 'Regular'),
            ('Andrew Brophy', 1986, 'London, England', 'Regular'),
            ('Mike Mo Capaldi', 1990, 'Simi Valley, CA', 'Regular'),
            ('Cory Kennedy', 1991, 'Lake Stevens, WA', 'Regular'),
            ('Rick McCrank', 1976, 'Vancouver B.C., Canada', 'Regular'),
            ('Jeron Wilson', 1977, 'Van Nuys, CA', 'Regular'),
            ('Mike Carroll', 1976, 'Friskonia, CA', 'Goofy'),
            ('Rick Howard', 1972, 'Vancouver Lakers, Canada', 'Goofy'),
            ('Tyler (Manchild) Pacheco', 1997, 'Santa Clarita, CA', 'Regular'),
            ('Simon Bannerot', 1999, 'Seattle, WA', 'Goofy'),
            ('Griffin Gass', 1997, 'Seattle, WA', 'Regular'),
            ('Niels Bennett', 1997, 'Pesacola, FL', 'Goofy'),
            ('Breanna Geering', 1999, 'Kelowna, Canada', 'Goofy'),
            ('Rowan Davis', 2000, 'New Castle, Australia', 'Regular')]


habitat = []


heroin =   [('Chet Childress', 1972, 'Wilmington, NC', 'Regular'),
            ('Daniel Shimizu', 1982, 'Los Feliz, CA', 'Regular'),
            ('Craig Scott', 1990, 'N/A', 'Regular'),
            ('Tony Karr', 1993, 'Los Angeles, CA', 'Goofy'),
            ('Lee Yankou', 1990, 'Toronto, Canada', 'Regular'),
            ('Tom Day', 1990, 'N/A', 'Regular')]


madness =  [('Clay Kreiner', 1997, 'Simpsonville, SC', 'Regular'),
            ('Sam Beckett', 1993, 'Norfolk, England', 'Goofy'),
            ('Jack Fardell', 1991, 'Queanbeyan, Australia', 'Regular'),
            ('Alex Perelson', 1991, 'San Diego, CA', 'Regular'),
            ('Ace Pelka', 1997, 'Oceanside, CA', 'Goofy'),
            ('Trey Wood', 2001, 'Queen Creek, AZ', 'Regular')]


krooked =  [('Mark Gonzales', 1968, 'South Gate, CA', 'Goofy'),
            ('Bobby Worrest', 1987, 'Washington DC', 'Goofy'),
            ('Dan Drehobl', 1972, 'Brunswich, Maine', 'Regular'),
            ('Mike Anderson', 1990, 'Ventura, CA', 'Goofy'),
            ('Brad Cromer', 1988, 'Palm Beach Gardens, FL', 'Regular')]

            
pizza = []


planB =    [('Chris Joslin', 1997, 'Cerritos, CA', 'Regular'),
            ('Felipe Gustavo', 1991, 'Brasilia, Brazil', 'Goofy'),
            ('Aurelien Giraud', 2000, 'Lyon, France', 'Goofy'),
            ('Tommy Fynn', 1989, 'Brisbane, Australia', 'Goofy'),
            ('Ryan Sheckler', 1990, 'San Clemente, CA', 'Regular'),
            ('Pat Duffy', 1974, 'San Francisco, CA', 'Goofy'),
            ('Trevor McClung', 1991, 'Huntington Beach, CA', 'Regular'),
            ('PJ Ladd', 1983, 'Boston, MA', 'Regular'),
            ('Danny Way', 1975, 'Portland, OR', 'Regular'),
            ('Colin McKay', 1979, 'Vancouver B.C, Canada', 'Goofy'),
            ('Sean Sheffey', 1980, 'San Diego, CA', 'Regular')]



primitive =[('Paul Rodriguez', 1985, 'Los Angeles, CA', 'Goofy'),
            ('Tiago Lemos', 1992, 'Jaguariuna SP, Brazil', 'Goofy'),
            ('Miles Silvas', 1996, 'Sacramento, CA', 'Regular'),
            ('Carlos Ribeiro', 1992, 'Novo Hamburgo, Brazil', 'Regular'),
            ('Wade Desarmo', 1985, 'Ottawa Ontario, Canada', 'Goofy'),
            ('Spencer Hamilton', 1989, 'Ottawa Ontario, Canada', 'Regular'),
            ('Franky Villani', 1996, 'Santa Ana, CA', 'Regular'),
            ('Trent McClung', 1994, 'Huntington Beach, CA', 'Goofy'),
            ('Robert Neal', 1999, 'Long Beach, CA', 'Regular'),
            ('Marek Zaprazny', 1990, 'Malacky Slovak, Republic Slovakia', 'Goofy'),
            ('JB Gillet', 1990, 'Lyon, France', 'Regular'),
            ('Brian Peacock', 1989, 'Newark, DE', 'Regular'),
            ('Giovanni Vianna', 2001, 'Santo Andrew, Brazil', 'Regular')]


real =     [('Dennis Busenitz', 1981, 'Newton, KS', 'Goofy'),
            ('Ishod Wair', 1991, 'Bordentown, NJ', 'Goofy'),
            ('Chima Ferguson', 1989, 'Coffs Harbour', 'Regular'),
            ('Kyle Walker', 1994, 'Oklahoma City, OK', 'Goofy'),
            ('Mason Silva', 1996, 'Manhattan Beach, CA', 'Regular'),
            ('Jack Olson', 1995, 'St. Louis Park, MN', 'Regular'),
            ('Tanner Van Vark', 1998, 'Andover, MN', 'Regular'),
            ('Jake Donnelly', 1988, 'Buffalo, NY', 'Regular'),
            ('Davis Torgerson', 1990, 'Wayzata, MN', 'Goofy'),
            ('Justin Brock', 1988, 'Atlanta, GA', 'Regular'),
            ('Robbie Brockel', 1990, 'Phoenix, AZ', 'Goofy'),
            ('Zion Wright', 1999, 'Jupiter, FL', 'Regular'),
            ('Keith Hufnagel', 1974, 'Manhattan, NY', 'Goofy'),
            ('Max Schaaf', 1973, 'Oakland, CA', 'Goofy')]


santaCruz =[('Blake Johnson', 1992, 'Venice, CA', 'Regular'),
            ('Emmanuel Guzman', 1985, 'Santa Cruz, CA', 'Regular'),
            ('Eric Dressen', 1967, 'Los Angeles, CA', 'Regular'),
            ('Erick Winkowski', 1995, 'San Diego, CA', 'Goofy'),
            ('Fabiana Delfino', 1997, 'Boca RAton, FL', 'Regular'),
            ('Henry Gartland', 2000, 'Minneapolis, MN', 'Regular'),
            ('Jake Wooten', 2001, 'Gallatin, TN', 'Regular'),
            ('Jereme Knibbs', 1993, 'Tampa, FL', 'Goofy'),
            ('Kevin Braun', 1995, 'Naperville, IL', 'Goofy'),
            ('Maurio McCoy', 1995, 'Reading, PA', 'Regular'),
            ('Steve Alba', 1963, 'Pomona, CA', 'Regular'),
            ('Tom Remillard', 1991, 'San Diego, CA', 'Regular'),
            ('Tom Knox', 1991, 'London, England', 'Goofy'),
            ('Tom Asta', 1990, 'Langhorne, PA', 'Regular'),
            ('Yndiara Asp', 1998, 'Florianopolis, Brazil', 'Goofy')]


sk8Mafia = [('Kellen James', 1990, 'San Diego, CA', 'Goofy'),
            ('Brandon Turner', 1978, 'San Diego, CA', 'Regular'),
            ('Peter Smolik', 1977, 'San Diego, CA', 'Goofy'),
            ('Jimmy Cao', 1988, 'San Diego, CA', 'Regular'),
            ('Jamie Palmore', 1987, 'San Diego, CA', 'Goofy'),
            ('Marshall Heath', 1989, 'Huntington, VT', 'Goofy'),
            ('Larelle Gray', 1988, 'San Diego, CA', 'Regular'),
            ('Wes Kremer', 1990, 'San Diego, CA', 'Goofy'),
            ('Tyler Surrey', 1988, 'San Diego, CA', 'Goofy'),
            ('Javier Sarmiento', 1981, 'Vitoria, Spain', 'Goofy')]


toyMachine=[('Ed Templeton', 1973, 'Huntington Beach, CA', 'Regular'),
            ('Billy Marks', 1983, 'Corona, CA', 'Regular'),
            ('Josh Harmony', 1984, 'Rancho Cucamonga, CA', 'Regular'),
            ('Leo Romero', 1987, 'Fontana, CA', 'Regular'),
            ('Matt Bennett', 1986, 'Corona, CA', 'Regular'),
            ('Collin Provost', 1991, 'Huntington Beach, CA', 'Goofy'),
            ('Daniel Lutheran', 1990, 'Albuquerque, NM', 'Goofy'),
            ('Blake Carpenter', 1993, 'Flagler Beach, FL', 'Goofy'),
            ('Jeremy Leabres', 1994, 'Corona, CA', 'Goofy'),
            ('Axel (Crusher) Cruysberghs', 1994, 'Poperinge, Belgium', 'Regular'),
            ('CJ Collins', 2004, 'Anaheim, CA', 'Regular'),
            ('Myles Willard', 1997, 'Baltimore, MD', 'Regular')]


welcome =  [('Nora Vasconcellos', 1993, 'Boston, MA', 'Regular'),
            ('Daniel Vargas', 1994, 'Lake Forrest, CA', 'Regular'),
            ('Roman Pabich', 2002, 'Ocean City, MD', 'Goofy'),
            ('Jason Salillas', 1999, 'Birmingham, AL', 'Goofy'),
            ('Jordan Sanchez', 1996, 'Everett, WA', 'Regular'),
            ('Rick Fabro', 1996, 'San Pedro, CA', 'Goofy'),
            ('Ryan Lay', 1989, 'Mesa, AZ', 'Regular'),
            ('Will Blaty', 1994, 'Gilbert, AZ', 'Regular'),
            ('Ryan Townley', 1991, 'Anaheim Hills, CA', 'Regular'),
            ('Aaron Goure', 1996, 'Tempe, AZ', 'Goofy')]


zero =     [('Jamie Thomas', 1974, 'Dothan, AL', 'Regular'),
            ('Tommy Sandoval', 1986, 'Chula Vista, CA', 'Regular'),
            ('Dane Burman', 1988, 'Sydney, Australia', 'Goofy'),
            ('Chris Cole', 1982, 'Langhorne, PA', 'Regular'),
            ('James Brockman', 1983, 'Lakeside, CA', 'Regular'),
            ('Tony Cervantes', 1990, 'Whittier, CA', 'Regular'),
            ('Windsor James', 1987, 'Colorado Springs, CO', 'Regular'),
            ('Adrian Lopez', 1985, 'Los Angeles, CA', 'Regular'),
            ('Adam Arunski', 1990, 'Mesa, AZ', 'Regular'),
            ('Gabriel Summers', 1991, 'Melbourne, Australia', 'Goofy'),
            ('Jonno Gaitan', 1996, 'San Marcos, CA', 'Regular'),
            ('Reggie Kelly', 1994, 'Colombus, GA', 'Regular')]


#Make a list of the team info, and the corresponding table name (tuples)
teams = [(almost, 'Almost'),
         (april, 'April'),
         (antiHero, 'AntiHero'),
         (baker, 'Baker'),
         (birdhouse, 'Birdhouse'),
         (blind, 'Blind'),
         (bloodWizard, 'BloodWizard'),
         (chocolate, 'Chocolate'),
         (creature, 'Creature'),
         (deathWish, 'Deathwish'),
         (element, 'Element'),
         (enjoi, 'Enjoi'),
         (FA, 'FA'),
         (flip, 'Flip'),
         (foundation, 'Foundation'),
         (girl, 'Girl'),
         (habitat, 'Habitat'),
         (heroin, 'Heroin'),
         (madness, 'Madness'),
         (krooked, 'Krooked'),
         (pizza, 'Pizza'),
         (planB, 'PlanB'),
         (primitive, 'Primitive'),
         (real, 'Real'),
         (santaCruz, 'SantaCruz'),
         (sk8Mafia, 'Sk8Mafia'),
         (toyMachine, 'ToyMachine'),
         (zero, 'Zero')]


#Loop through each tuple of teams
for team in teams:
    #Sort the lists alphabetically by first name
    team[0].sort(key=lambda x: x[0])

    #Insert the info (if it's not already in)
    [sql_insert(con, team[1], skaters) for skaters in team[0]]    

    #Update their age by subtracting their birthyear by the current year
    [sql_update(con, team[1], 'Age', datetime.today().year - skater[1], 'Name', skater[0]) for skater in team[0]]



    print('\n==============================================', f"                 {team[1].upper()}", '==============================================\n', sep='\n')
    sql_fetch(con,team[1])