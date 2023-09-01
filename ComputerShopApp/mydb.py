# Install mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

# first you need to run above commands

# then write this code 

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="", 
    
)

# preppare a cursor object
cursorObject = dataBase.cursor()

# create Database databe name will be after the CREATE DATABASE
cursorObject.execute("CREATE DATABASE computer_shop")

print("All Done!")
