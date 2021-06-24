import mysql.connector
import time
import login
db = mysql.connector.connect(
    host="127.0.0.1", #localhost ip
    user="root",
    password="administrator",
    database="userdb"
)
cursor = db.cursor()
def createdatabase():
    time.sleep(0.33)
    cursor.execute("""CREATE DATABASE userdb""")
def createtable():
    time.sleep(0.33)
    cursor.execute("CREATE TABLE users (username VARCHAR(30), password VARCHAR(255))")
def readcol():
    time.sleep(0.33)
    cursor.execute("SELECT username, password FROM users")
    result = cursor.fetchall()
    print(result)
i = input("Do you wanna go to the login-page? [yes or no] \n>>>")
ii = i.upper()
if ii == "YES":
    print("`commands` = shows a list of commands")
    counter_exit = 0
    while counter_exit != 1:
        x = input(">>>")
        xx = x.upper()
        if xx == "EXIT":
            counter_exit += 1
            db.commit()
        elif xx == "REGISTER":
            user_name = input("Username: ")
            user_password = input("Password: ")
            cursor.execute("INSERT INTO users (username, password) VALUES (" + "'" + user_name + "'" + "," + "'" + user_password + "'" + ")")
            db.commit()
        elif xx == "LOGIN":
            user_name = input("Username: ")
            user_password = input("Password: ")
            cursor.execute("SELECT username, password FROM users")
            i = cursor.fetchall()
            ii = len(i)
            iii = ii - 1
            tup = (user_name, user_password)
            counter = 0
            while counter <= iii:
                if tup == i[counter]:
                    login.loginpage()
                    counter_exit +=1
                else:
                    l = 0
                counter +=1
        elif xx == "COMMANDS":
            print("'EXIT' = Exits the program \n'REGISTER' = Registers a user \n'LOGIN' = Brings you to the login-page")
else:
    exit()