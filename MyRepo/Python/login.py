import hashlib
from datetime import datetime
import getpass
import os
import time

def timestamp():
    now = datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')
    return date

def new_user(name):
    while True:
        uName = input("What is your user name going to be?\n")
        pass1 = hashlib.md5(getpass.getpass("what is your password: ").encode('UTF-8')).hexdigest()
        pass2 = hashlib.md5(getpass.getpass("Confirm your password: ").encode('UTF-8')).hexdigest()
        if pass1 == pass2:
            with open("shadow.txt","a") as fShadow:
                fShadow.write(f"{uName} {pass1}\n")
            with open("log.txt","a") as flog:
                flog.write(f"New user: {uName},created by: {name}, at: {timestamp()}\n")
                break

        else:
            print("your passwords did not match")
def login():
    while True:
        unames = []
        shadows = []
        state = False
        while True:
            try:
                with open('shadow.txt','a') as fShadow:
                    for line in fShadow:
                        seperater = line.split()
                        unames.append(seperater[0])
                        shadows.append(seperater[1])
                break
            except FileNotFoundError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("No file found, starting for a new user.")
                time.sleep(2)
                new_user("System")
                continue
        while state != True:
            print (state,unames,shadows)
            user = input("what is your user name?\n")
            if user in unames:
                ##TODO: add password
                count = 0
                position = unames.index(user)
                while count < 2:
                    count +=1
                    password = hashlib.md5(getpass.getpass("Please enter you password").encode('UTF-8')).hexdigest()
                    if password == shadows[position]:
                        state = True
                        break
            else:
                with open('log.txt','a') as flog:
                    flog.write(f"ATTEMPTED LOGIN WITHOUT CRADENTIALS: {timestamp()}")
                    getpass.getpass("Please enter your password:")
                    getpass.getpass("Please enter your password:")
                    getpass.getpass("Please enter your password:")
                    print("Your password did not match, exiting program")
                    time.sleep(2)
                    quit()
login()
