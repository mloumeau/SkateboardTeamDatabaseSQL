# SkateboardTeamDatabaseSQL

# Overview


This program generates a .db file that works with SQLite3. It creates tables for all skateboard teams if the table doesn't already exist, it inserts information for each member of the team, and it updates the information upon request.

I have been skateboarding for most of my life. Throughout this process, I have become a full-blown skateboarding nerd. I love all the information I can gather about anything related to a skateboard. However, I've noticed there is no central hub for general skate information. I decided to create this project not only as a convenient source of reliable information all in one place, but also to learn SQL as well.


[Software Demo Video](http://youtube.link.goes.here)

# Relational Database


I originally was thinking this project would be 3 layers deep: the team, the skater, and the skater's information. However, after learning a bit more about SQL, I learned that it would be more practical to use 2 layers. I made the tables the team, and placed all the information of the skaters inside of the table, including their name. In order to compensate their name being more important than the other information, I made it the primary key and placed it at the front of the list of information.


# Development Environment


For this project, I used SQLite3 (in the command line), the python sqlite3 module, and a convenient tool to interact with the database called 'DB Browswer for SQLite'.

# Useful Websites

* [SQLite3 Python Tutorial](https://likegeeks.com/python-sqlite3-tutorial/)
* [Wikipedia for Skateboard Team Info](https://en.wikipedia.org/wiki/Baker_Skateboards)

# Future Work

* Verify information with members in the community
* Create a website to display the info
* Learn to implement SQL databases with HTML/JavaScript
