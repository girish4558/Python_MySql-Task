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

# Validating Mobile Number
def valid_mobile(mobile):
    return str(mobile).isdigit() and len(str(mobile)) == 10

# Insert new Contact into database
def insert(name, Mobile_Number, Email_id):
        if not valid_mobile(Mobile_Number):
            print("Invalid mobile number. Must be 10 digits.")
            return
        
        # Handle DataBase connection errors
        try:
            cursor.execute("INSERT INTO Contact (Person_Name,Mobile_Number,Email_Id) VALUES (%s,%s,%s)",(name,Mobile_Number, Email_id))
            mysql_Connection.commit()
            print("Contact is Saved Successfully..!")
        except mysql.connector.errors.DatabaseError as err:
            print("Invalid Data. Try Again")

# Display All the Contacts from the database
def display():
    print("============Contact List============")
    cursor.execute("SELECT * FROM Contact")
    contacts = cursor.fetchall()
    if not contacts:
        print("No Contacts Found")
    for row in contacts:
        id = row[0]
        name = row[1]
        Mobile = row[2]
        Email = row[3]
        print(f"User_Id     : {id}")
        print(f"User Name   : {name}")
        print(f"Mobile      : {Mobile}")
        print(f"Email       : {Email}")
        print("-" * 40)

# Search Contact By using "Name"
def search_name(name):
    cursor.execute("SELECT * FROM Contact WHERE Person_Name LIKE %s", ("%" + name + "%",))
    contacts = cursor.fetchall()
    if not contacts:
        print("No Contacts Found")
    for row in contacts:
        id = row[0]
        name = row[1]
        Mobile = row[2]
        Email = row[3]
        print(f"User_Id     : {id}")
        print(f"User Name   : {name}")
        print(f"Mobile      : {Mobile}")
        print(f"Email       : {Email}")
        print("-" * 40)

# Search Contact By using "Mobile"
def search_mobile(mobile):
    if not valid_mobile(mobile):
        print("Invalid mobile number. Must be 10 digits.")
        return
    contacts = cursor.fetchall()
    if not contacts:
        print("No Contacts Found")
    for row in contacts:
        id = row[0]
        name = row[1]
        Mobile = row[2]
        Email = row[3]
        print(f"User_Id     : {id}")
        print(f"User Name   : {name}")
        print(f"Mobile      : {Mobile}")
        print(f"Email       : {Email}")
        print("-" * 40)

# Update Name from the database
def update(id,name):
    cursor.execute("UPDATE Contact set Person_Name = %s WHERE Person_Id = %s",(name,id ))
    mysql_Connection.commit()

# Delete Record from the database
def delete(id):
    cursor.execute("DELETE FROM Contact WHERE Person_Id = %s",(id,))
    mysql_Connection.commit()

# Excecution of Contact Saver Application
while True:
    print(" 1.Insert a new Contact\n 2.View All Contacts\n 3.Search Contact\n 4.Update Contact\n 5.Delete Contact\n 6.Exit")
    User_Choise = int(input("Choose your Option: "))

    match User_Choise:
        case 1:
            # Prompt used for contact details
            name = input("Enter User_Name: ")
            Mobile_Number = int(input("Enter Mobile Number: "))
            Email_id = input("Enter Email Id: ")
            insert(name, Mobile_Number, Email_id)

        case 2:
            display()

        case 3:
            print(" 1.Serach by using name\n 2.Search by using Mobile")
            choise = int(input("Enter your mode of search: "))
            match choise:
                case 1:
                    name = input("Enter name: ")
                    search_name(name)
                case 2:
                    Mobile_Number = int(input("Enter Mobile Number: "))
                    search_mobile(Mobile_Number)

        case 4:
            id = int(input("Enter id: "))
            name = input("Enter new Name to Update: ")
            update(id,name)
            print("You have Updated Successfully..!")

        case 5:
            id = int(input("Enter id to Delete: "))
            delete(id)
            print("You deleted the Contact successfully..!")

        case 6:
            # Close the connections
            cursor.close()
            mysql_Connection.close()
            print("You are Exited")
            break

        case _:
            print("XXX  ---Choose valid Option---  XXX")




        