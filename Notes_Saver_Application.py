import mysql.connector

# MySql Connection
mysql_Connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="contact"
)

# Creating Cusor Object
cursor = mysql_Connection.cursor()

# Insert Note
def insert_Note(title,Content):
    cursor.execute("INSERT INTO notes (Title, Content) VALUES (%s,%s)",(title,Content))
    mysql_Connection.commit()
    print("Note Added Successfully...!")

# Display
def Display():
    print("=================== Notes List ===================")
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()

    if not notes:
        print("No notes found.")
        return

    for row in notes:
        note_id = row[0]
        title = row[1]
        content = row[2]
        created_date = row[3].strftime("%d-%m-%Y %I:%M %p")  # clear date + time

        print(f"ID          : {note_id}")
        print(f"Title       : {title}")
        print(f"Content     : {content}")
        print(f"Created On  : {created_date}")
        print("-" * 40)

# Searching Notes
def search(note_title):
    cursor.execute("SELECT * FROM notes WHERE LOWER(Title) = LOWER(%s)",(note_title,))
    titles = cursor.fetchall()

    if not titles:
        print("No notes found.")
        return

    for row in titles:
        note_id = row[0]
        title = row[1]
        content = row[2]
        created_date = row[3].strftime("%d-%m-%Y %I:%M %p")  # clear date + time

        print(f"ID          : {note_id}")
        print(f"Title       : {title}")
        print(f"Content     : {content}")
        print(f"Created On  : {created_date}")
        print("-" * 40)

# Updating The Note
def update(title, content, id):
    cursor.execute("UPDATE notes set Title = %s, Content = %s WHERE Note_id = %s", (title, content, id))
    mysql_Connection.commit()
    print("You Updated Note Successfully..!")

# Deleting The Note
def delete(id):
    cursor.execute("DELETE FROM notes WHERE Note_id = %s",(id,))
    mysql_Connection.commit()
    print("You Deleted Note Successfully..!")
# Excecution of Notes Saver Application
while True:
    print(" 1.Insert a new Note\n 2.Display all the Notes\n 3.Search Notes\n 4.Update Note\n 5.Delete Note\n 6.Exit")
    Choise = int(input("Enter your choise: "))

    match Choise:
        case 1:
            title = input("Enter Note Title: ")
            Content = input("Enter Content: ")
            insert_Note(title, Content)

        case 2:
            Display()

        case 3:
            title = input("Enter Title to search: ")
            search(title)

        case 4:
            id = int(input("Enter Note id: "))
            title = input("Enter new title to Update: ")
            content = input("Enter new Content to Update: ")
            update(title,content,id)

        case 5:
            id = int(input("Enter id to Delete: "))
            delete(id)

        case 6:
            cursor.close()
            mysql_Connection.close()
            print("You are Exited")
            break

        case _:
            print("XXX  ---Choose valid Option---  XXX")
