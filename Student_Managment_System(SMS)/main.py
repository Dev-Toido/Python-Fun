import mysql.connector as sql
import dbs  # Import the dbs module to ensure database and tables are created
from funs import (
    welcome, sd_entry, sd_search, sd_update, sd_display,
    td_entry, td_sentry, td_supdate, a_update, s_report_card
)

def main():
    welcome()
    # Connect to MySQL and select the database
    con = sql.connect(host="localhost", user="root", password="Mysql#123", database="sms")
    cur = con.cursor()
    dbs.create_tables()  # Ensure tables are created

    while True:
        print("\n--- Student Management System Menu ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Display All Students")
        print("5. Add Test")
        print("6. Add Student Column to Test Table")
        print("7. Update Student Marks")
        print("8. Update Analysis")
        print("9. Show Student Report Card")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            sd_entry(con, cur)
        elif choice == "2":
            name = input("Enter full or partial name to search: ")
            sd_search(con, cur, name)
        elif choice == "3":
            name = input("Enter full or partial name to update: ")
            sd_update(con, cur, name)
        elif choice == "4":
            sd_display(con, cur)
        elif choice == "5":
            td_entry(con, cur)
        elif choice == "6":
            name = input("Enter student name: ")
            cont = input("Enter student contact: ")
            td_sentry(con, cur, name, cont)
        elif choice == "7":
            name = input("Enter student name: ")
            cont = input("Enter student contact: ")
            marks = int(input("Enter marks: "))
            test_no = int(input("Enter test number: "))
            td_supdate(con, cur, name, cont, marks, test_no)
        elif choice == "8":
            a_update(con, cur)
        elif choice == "9":
            name = input("Enter full or partial name for report card: ")
            s_report_card(con, cur, name)
        elif choice == "0":
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

    cur.close()
    con.close()

if __name__ == "__main__":
    main()