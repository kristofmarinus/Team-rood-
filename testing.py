import sqlite3

def adjust_user(conn):
    # Choose id of the user
    user_id = int(input("Enter the id of the user: "))

    # Do you want to adjust whole row or specific column
    adjust_type = int(input("Do you want to adjust 1. whole row or 2. specific column: "))

    if adjust_type == 1:
        # Ask for all the details
        fname = input("Enter the first name: ")
        lname = input("Enter the last name: ")
        email = input("Enter the email: ")
        phone = input("Enter the phone number: ")

        # Update the row in the database
        c = conn.cursor()
        c.execute("UPDATE users SET fname=?, lname=?, email=?, phone=? WHERE id=?", (fname, lname, email, phone, user_id))
        conn.commit()
        print("User details updated successfully!")
    elif adjust_type == 2:
        # Ask for the column to be adjusted
        column = input("Enter the column name to be adjusted: ")
        value = input("Enter the new value: ")

        # Update the column in the database
        c = conn.cursor()
        c.execute("UPDATE users SET {}=? WHERE id=?".format(column), (value, user_id))
        conn.commit()
        print("User details updated successfully!")

def main():
    # Connect to the database
    conn = sqlite3.connect("users.db")

    while True:
        # Adjust user details
        adjust_user(conn)

        # Ask if user wants to adjust more column or choose another row/user
        more = int(input("Do you want to 1. adjust more column of the user or 2. choose another row/user or 3. exit: "))
        if more == 1:
            continue
        elif more == 2:
            continue
        elif more == 3:
            break

if __name__ == "__main__":
    main()
