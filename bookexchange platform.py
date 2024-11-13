loginDict = {}

def createAccount(loginDict):
    username = input("What username do you want to use?")
    if username in loginDict:
        print("Username is already taken.")
    else:
        password = input("What password would you like to use?")
        loginDict[username] = password

def login(loginDict):
    username = input("what is your username?")
    if username not in loginDict:
        print("Username does not exist")
        return None
    else:
        password = input("What is your password")
        if password == loginDict[username]:
            print("You are logged in.")
            return username
        else:
            print("The password is wrong.")
            return None
