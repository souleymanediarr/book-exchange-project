# Key: username, Value: password
loginDict = {}
# Key: username, Value: list of books that user has
usersBooks = {}
# Key: bookname, Value: (Author, Genre)
bookInfo = {}
# Key: bookname, Value: how many in the exchange
bookCount = {}

def createAccount():
    username = input("What username do you want to use? ")
    if username in loginDict:
        print("Username is already taken.")
    else:
        password = input("What password would you like to use? ")
        loginDict[username] = password
        usersBooks[username] = []

def login():
    username = input("what is your username? ")
    if username not in loginDict:
        print("Username does not exist")
        return None
    else:
        password = input("What is your password? ")
        if password == loginDict[username]:
            print("You are logged in.")
            return username
        else:
            print("The password is wrong.")
            return None

# Function to add a book to the exchange
def addBook(bookName):
    if bookName in bookCount:
        bookCount[bookName] = bookCount[bookName] + 1
    else:
        bookCount[bookName] = 1

# Function to remove a book from the exchange
def removeBook(bookName):
    if bookName in bookCount:
        currentCount = bookCount[bookName]
        bookCount[bookName] = currentCount - 1
        if currentCount - 1 == 0:
            del bookCount[bookName]

# Function to give a user a book
def giveBook(userName, bookName):
    if bookName in bookCount:
        usersBooks[userName].append(bookName)
    else:
        print(bookName + ' needs to be added first.')

# Function to get a user's list of books
def getUsersBooks(userName):
    return usersBooks[userName]

# Function to take a book from a user
def takeBook(userName, bookName):
    bookList = usersBooks[userName]
    if bookName in bookList:
        bookList.remove(bookName)

# Function to insert a book and its info
def insertBookInfo(bookName, author, genre):
    bookInfo[bookName] = (author, genre)

# Function to get a book's info in the form (Author, Genre)
def getBookInfo(bookName):
    if bookName in bookInfo:
        return bookInfo[bookName]
    else:
        return None
    
# Function to get a book's count
def getBookCount(bookName):
    if bookName in bookCount:
        return bookCount[bookName]
    else:
        return 0

if __name__ == '__main__':
    createAccount()
    username = login()
    book = input('Enter a book name: ')
    addBook(book)
    print('Count of ' + book + ': ' + str(bookCount[book]))
    removeBook(book)
    print('After removing ' + book + ', its count is: ' + str(getBookCount(book)))
    book = input('Enter another book name: ')
    addBook(book)
    giveBook(username, book)
    print(username + '\'s books: '+ str(getUsersBooks(username)))
    takeBook(username, book)
    print('After taking out ' + username + '\'s book, their list of books are: ' + str(getUsersBooks(username)))
    author = input('Enter ' + book + '\'s author: ')
    genre = input('Enter ' + book + '\'s genre: ')
    insertBookInfo(book, author, genre)
    print(book + '\'s info: ' + str(getBookInfo(book)))
