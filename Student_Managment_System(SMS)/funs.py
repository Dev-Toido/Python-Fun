def welcome():
    """
    Prints a welcome banner for the Student Management System.
    """
    for i in [
        '  !!!\tW     W  EEEEE  L      CCCCC  OOOOO  M     M  EEEEE  !!! ',
        ' !!!!!\tW     W  E      L      C   C  O   O  M M M M  E     !!!!!',
        ' !!!!!\tW  W  W  EEE    L      C      O   O  M  M  M  EEE   !!!!!',
        '  !!!\tW W W W  E      L      C      O   O  M     M  E      !!! ',
        '  (.)\t W   W   EEEEE  LLLLL  CCCCC  OOOOO  M     M  EEEEE  (.) '
    ]:
        print('    \t'*5 + i)

def create_concur(password="Mysql#123"):
    """
    Creates and returns a MySQL connection and cursor.
    """
    import mysql.connector as sql
    con = sql.connect(host="localhost", user="root", password=password)
    cur = con.cursor()
    return con, cur

def sd_entry(con, cur):
    """
    Adds a new student to the database and initializes their analysis record.
    """
    name = input("Enter the name of the student: ")
    cond = input("Enter the mobile number of the student: ")
    cur.execute("INSERT INTO s_d(name, contdes) VALUES (%s, %s)", (name, cond))
    con.commit()
    # Fetch the s_roll of the newly inserted student
    cur.execute("SELECT s_roll FROM s_d WHERE name=%s AND contdes=%s", (name, cond))
    result = cur.fetchone()
    if result:
        cur.execute("INSERT INTO analysis(s_roll) VALUES (%s)", (result[0],))
        con.commit()
    else:
        print("Error: Could not retrieve student roll number after insertion.")
    td_sentry(con, cur,roll=result[0] )

def search_by_name(cur, name_part):
    """
    Searches for students whose names contain the given substring (case-insensitive).
    Returns a list of matching student records.
    """
    cur.execute("SELECT * FROM s_d WHERE name LIKE %s", (f"%{name_part}%",))
    return cur.fetchall()

def sd_search(con, cur, name_part):
    """
    Searches for students by full or partial name and prints their details.
    """
    results = search_by_name(cur, name_part)
    if results:
        print("Matching students:")
        for row in results:
            print(row)
    else:
        print("No students found with that name.")

def sd_update(con, cur, name_part):
    """
    Updates the name and/or contact number of a student found by full or partial name.
    If multiple students match, prompts the user to select one.
    """
    matches = search_by_name(cur, name_part)
    if not matches:
        print("Student not found.")
        return
    if len(matches) > 1:
        print("Multiple students found:")
        for idx, row in enumerate(matches, 1):
            print(f"{idx}: {row}")
        sel = input("Enter the number of the student to update: ")
        try:
            sel = int(sel)
            result = matches[sel - 1]
        except (ValueError, IndexError):
            print("Invalid selection.")
            return
    else:
        result = matches[0]
    print(f"Current details: {result}")
    new_name = input("Enter new name (or press Enter to keep current): ")
    new_contdes = input("Enter new contact number (or press Enter to keep current): ")
    s_roll = result[0]
    if new_name:
        cur.execute("UPDATE s_d SET name=%s WHERE s_roll=%s", (new_name, s_roll))
    if new_contdes:
        cur.execute("UPDATE s_d SET contdes=%s WHERE s_roll=%s", (new_contdes, s_roll))
    con.commit()

def sd_display(con, cur):
    """
    Displays all students in the database.
    """
    cur.execute("SELECT * FROM s_d")
    results = cur.fetchall()
    if results:
        print("Student Details:")
        for row in results:
            print(row)
    else:
        print("No students found.")

def td_entry(con, cur):
    """
    Adds a new test with full marks to the test details table.
    """
    fm = int(input("Enter the test full marks: "))
    cur.execute("INSERT INTO t_d(fm) VALUES (%s)", (fm,))
    con.commit()

def td_sentry(con, cur, n, c,roll=None):
    """
    Adds a new column for a student's marks in the test details table.
    Uses search_by_name to find the student.
    """
    if roll:
        # If roll number is provided, use it directly
        sn = roll
    else:
        matches = search_by_name(cur, n)
        # Filter by contact if multiple matches
        if not matches:
            print("Student not found.")
            return
        # If multiple matches, filter by contact number
        result = None
        for row in matches:
            if str(row[2]) == str(c):
                result = row
                break
        if not result:
            print("Student not found with that name and contact.")
            return
        sn = result[0]
    # Check if column already exists to avoid SQL error
    cur.execute("SHOW COLUMNS FROM t_d LIKE %s", (f"S_{sn}",))
    if not cur.fetchone():
        cur.execute(f"ALTER TABLE t_d ADD S_{sn} INT")
        con.commit()
    else:
        print(f"Column for student {sn} already exists in t_d.")

def td_supdate(con, cur, n, c, m, tn):
    """
    Updates a student's marks for a specific test.
    """
    cur.execute("SELECT s_roll FROM s_d WHERE name=%s AND contdes=%s", (n, c))
    result = cur.fetchone()
    if result:
        sn = result[0]
        # Check if the column exists before updating
        cur.execute("SHOW COLUMNS FROM t_d LIKE %s", (f"S_{sn}",))
        if cur.fetchone():
            cur.execute(f"UPDATE t_d SET S_{sn}=%s WHERE test_no=%s", (m, tn))
            con.commit()
        else:
            print(f"No column for student {sn} in t_d. Please add it first.")
    else:
        print("Student not found.")

def a_update(con, cur):
    """
    Updates the analysis table with total marks, full marks, percentage, and status for each student.
    """
    cur.execute("SELECT s_roll FROM s_d")
    results = cur.fetchall()
    if results:
        for row in results:
            sn = row[0]
            cur.execute(f"SELECT fm, S_{sn} FROM t_d")
            marks = cur.fetchall()
            if marks:
                total_marks = full_marks = 0
                for mark in marks:
                    if mark[1] is not None:
                        full_marks += mark[0]
                        total_marks += mark[1]
                page = (total_marks / full_marks) * 100 if full_marks > 0 else 0
                cur.execute(
                    "UPDATE analysis SET tm=%s, fm=%s, page=%s WHERE s_roll=%s",
                    (total_marks, full_marks, page, sn)
                )
                con.commit()
                # Update status based on percentage
                if page >= 66:
                    cur.execute("UPDATE S_D SET status='Strong' WHERE s_roll=%s", (sn,))
                elif page >= 33:
                    cur.execute("UPDATE S_D SET status='Average' WHERE s_roll=%s", (sn,))
                else:
                    cur.execute("UPDATE S_D SET status='Weak' WHERE s_roll=%s", (sn,))
                con.commit()
    else:
        print("No students found for analysis update.")

def s_report_card(con, cur, name_part):
    """
    Prints the report card for a student by full or partial name.
    If multiple students match, prompts the user to select one.
    """
    matches = search_by_name(cur, name_part)
    if not matches:
        print("Student not found.")
        return
    if len(matches) > 1:
        print("Multiple students found:")
        for idx, row in enumerate(matches, 1):
            print(f"{idx}: {row}")
        sel = input("Enter the number of the student to view report card: ")
        try:
            sel = int(sel)
            result = matches[sel - 1]
        except (ValueError, IndexError):
            print("Invalid selection.")
            return
    else:
        result = matches[0]
    sn = result[0]
    cur.execute("SELECT * FROM analysis WHERE s_roll=%s", (sn,))
    report = cur.fetchone()
    if report:
        print(f"Report Card for {result[1]}:")
        print(f"Total Marks: {report[1]}, Full Marks: {report[2]}, Percentage: {report[3]}%, Status: {report[4]}")
    else:
        print("No report card found for this student.")