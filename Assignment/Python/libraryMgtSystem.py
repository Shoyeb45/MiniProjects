import pandas as pd
import datetime

# Function to print create data frame

def catalogueBooks(books):
    df = pd.DataFrame(books)
    df.set_index("ID", inplace=True)
    print(df)

# User Data
userData = [["Shoyeb", "459"], ["Prakhar", "321"]]

# Creating new account
response = input("Already existing user? (Response Y(yes) or N(no)):")
if response == "Y" or response == 'y':
    name = input("Please enter your name:")
    id = input("Please enter your user ID:")

    for it in userData:
        if it[0] == name and it[1] == id:
            print("\n****Valid Credentials****\n")
            break
        else:
            if it == userData[len(userData) - 1]:
                print("Your credentials doesn't exist in our database")
                response = "N"
                break
if response == "N" or response == "n":
    print("Please register for new account.")
    name = input("Please enter your username:")
    id = input("Please enter your user ID:")
    userData.append([name, id])
    print(f"Your credential added to our database:\nUsername:{userData[len(userData)-1][0]}\nUser ID:{userData[len(userData)-1][1]}")


books = {
    "ID"    : [101, 102, 103, 104, 105],
    "Title" : ["To Kill a Mockingbird", "One Hundred Years of Solitude", "Invisible Man", "Dunes", "Curtain: Poirot's Last Case"],
    "Author": ["Harper Lee", " Gabriel García Márquez", "H G Wells", "Frank Herbert", "Agatha Christie"],
    "Qty Available": [5, 3, 6, 4, 7]
}

# creating data frame to display library's current catalogue
print("Our current Catalogue:")
catalogueBooks(books)

# user data about books issued
libData = [["459", [105, datetime.date(2024, 3, 20)]], ["321", [103, datetime.date(2024, 3, 10)], [101, datetime.date(2024, 3, 25)]]]

# Taking response from user to checkout or return the book
resp = input("Do you want to return book or issue book(response r for return and c for issueing book):")

if resp == "R" or  resp == 'r':
    bookId = int(input("Please enter book id from catalogue:"))
    # checking if user have book or not
    for it in libData:
        if it[0] == id:
            for i in range(1, len(it)):
                if it[i][0] == bookId:
                    # finding the position of book in dictionary
                    pos = 0
                    for j in range(0, len(books["ID"])):
                        if books["ID"][j] == bookId:
                            pos = j
                            break
                        
                    # updating and printing 
                    print(f"Book name:{books['Title'][pos]}\nAuthor:{books["Author"][pos]}\n\n")        
                    books["Qty Available"][pos] = books["Qty Available"][pos] + 1
                    print("Updated Catalogue")
                    catalogueBooks(books)

                    # Calculating fine if overdue
                    diff = datetime.date.today() - it[i][1]
                    if (diff.days > 14):
                        print(f"You have returned the book after 14 days, so overdue fine will be charged. The fine is calulated $1 per day after overdue. So overdue days: {diff.days - 14}\nPlease pay ${diff.days - 14}.")
                else:
                    if it[i] == it[len(it[i]) - 1]:
                        print("You don't have specified book\nPlease issue the book first.")
                        resp = "c"     
            break
        else:   
            if it == libData[len(libData) - 1]:
                print("Please issue the book first.")
                resp = "c"

if resp == "c" or resp == "C":
    bookId = int(input("Please enter book id from catalogue :"))

    for i in range(0, len(books["ID"])):
        if books["ID"][i] == bookId:
            # finding position of book in dictionary
            pos = 0
            for j in range(0, len(books["ID"])):
                if books["ID"][j] == bookId:
                    pos = j
                    break

            # Displaying author and title
            print(f"Book name:{books['Title'][pos]}\nAuthor:{books["Author"][pos]}\n\n")

            # updating in user-data.
            # First checking existing user or not
            if response == "N" or response == "n":
                libData.append([id, [books["ID"][pos], datetime.date.today()]]) 
                books["Qty Available"][pos] = books["Qty Available"][pos] - 1
                # updated catalogue
                catalogueBooks(books)
                break
            else:
                # first finding the user position
                for it in libData:
                    if it[0] == id:
                        if len(it) >= 4:
                            print("You have more than 3 books")
                            break

                    # Updating in catalogue
                    it.append([books["ID"][pos], datetime.date.today()])
                    books["Qty Available"][pos] = books["Qty Available"][pos] - 1
                    # updated catalogue
                    catalogueBooks(books)
                    break
            break
        else:
            if i == len(books["Author"]) - 1:
                print("Not a valid book ID.")
                break