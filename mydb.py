import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@Codi121317'
    
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE bjdb")

print("Success!")