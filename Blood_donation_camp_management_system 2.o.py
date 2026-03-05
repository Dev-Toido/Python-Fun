import mysql.connector
import time
import datetime

def create_tables(cursor):
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS blood_donation_camp_management_system;")
    cursor.execute("use blood_donation_camp_management_system;")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Camp (
        camp_id INT AUTO_INCREMENT PRIMARY KEY,
        cdate DATE NOT NULL,
        location VARCHAR(200) NOT NULL,
        organizer VARCHAR(100)
    );
    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS Donor(
        donor_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        dofb DATE NOT NULL,
        age INT ,
        gender VARCHAR(10) NOT NULL ,
        blood_group VARCHAR(5) NOT NULL,
        contact_number VARCHAR(20) NOT NULL,
        address VARCHAR(100)
        );
    """)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Recipient (
        recipient_id INT AUTO_INCREMENT PRIMARY KEY,
        hname VARCHAR(100) NOT NULL,
        haddress VARCHAR(200) NOT NULL,
        hcontact_number VARCHAR(20) NOT NULL,
        authorized_person VARCHAR(100)
    );""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Donation (
        donation_id INT AUTO_INCREMENT PRIMARY KEY,
        donor_id INT NOT NULL,
        camp_id INT NOT NULL,
        blood_group VARCHAR(5) NOT NULL,
        quantity DECIMAL(5,2) NOT NULL,
        recipient_id INT,
        FOREIGN KEY (donor_id) REFERENCES Donor(donor_id),
        FOREIGN KEY (camp_id) REFERENCES Camp(camp_id),
        FOREIGN KEY (recipient_id) REFERENCES Recipient(recipient_id)
    );
    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS Inventory (
        inventory_id INT AUTO_INCREMENT PRIMARY KEY,
        blood_group VARCHAR(5) NOT NULL,
        quantity DECIMAL(5,2) NOT NULL,
        expiration_date DATE NOT NULL,
        donation_id INT,
        FOREIGN KEY (donation_id) REFERENCES Donation(donation_id)
    );""")

def calculate_date_after_n_days(start_date_str, n):
    """Calculates the date after a specified number of days from a given date.
    Args:
        start_date_str: The starting date in the format 'YYYY-MM-DD'.
        n: The number of days to add.
    Returns:
        The calculated date after n days in the format 'YYYY-MM-DD'.
    """
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = start_date + datetime.timedelta(days=n)
    return end_date.strftime('%Y-%m-%d')

def spacest(s,spn,m=0):
    try :
        spn=' '*spn
        assert m in [-1,0,1],-1
        if len(spn)<=len(s):
            return s
        else:
            if m==-1:
                return s+spn[len(s):]

            elif m==1:
                return spn[:len(spn)-len(s)]+s

            elif m==0:
                n=len(spn)-len(s)
                return spn[:n//2]+s+spn[len(s)+n//2:]
    except:
        return s+spn[len(s):]
    
def cuteprint(llos,m=-1):
    llos=list(llos)
    tlist=[]
    stlist=[]
    nlist=[]
    mainlist=[]
    c=len(llos[0])
    for los in llos:
        if c==len(los):
            tlist.append(list(los))
        else:
            return
    for i in range(c):
        nlist.append(0)
    for i in tlist:
        for j in range(c):
            if len(i[j])>nlist[j]:
                nlist[j]=len(i[j])
    for i in range(len(tlist)):
        for j in range(c):
            if j==0:
                tlist[i][j]="|"+spacest(tlist[i][j],nlist[j]+4,m)+"|"
                if i==0:
                    stlist.append("+"+"-"*(nlist[j]+4)+"+")
            else:
                tlist[i][j]=spacest(tlist[i][j],nlist[j]+4,m)+"|"
                if i==0:
                    stlist.append("-"*(nlist[j]+4)+"+")
        tlist[i][-1]=tlist[i][-1]+"\n"
    stlist[-1]=stlist[-1]+"\n"
    for i in tlist:
        mainlist.append(stlist)
        mainlist.append(i)
    mainlist.append(stlist)
    return mainlist

def datediff(user_date_str):
    """Calculates the difference between today and a user-given date.
    Args:
        user_date_str: The user-provided date in the format 'YYYY-MM-DD'.
    Returns:
        The number of days between today and the user-given date.
    """
    date_format = "%Y-%m-%d"
    user_date = datetime.datetime.strptime(user_date_str, date_format).date()
    today = datetime.date.today()
    difference = user_date - today
    return difference.days

def calculate_age(dob):
    dob = datetime.datetime.strptime(dob, '%Y-%m-%d')  # Convert the DOB string to a datetime object
    today = datetime.datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))  # Correct for birthdate not yet reached in current year
    return age

def welcome():
    for i in ['  !!!\tW     W  EEEEE  L      CCCCC  OOOOO  M     M  EEEEE  !!! ', ' !!!!!\tW     W  E      L      C   C  O   O  M M M M  E     !!!!!', ' !!!!!\tW  W  W  EEE    L      C      O   O  M  M  M  EEE   !!!!!', '  !!!\tW W W W  E      L      C      O   O  M     M  E      !!! ', '  (.)\t W   W   EEEEE  LLLLL  CCCCC  OOOOO  M     M  EEEEE  (.) ']:
        print('    \t'*5+i)

def intro():#To print the initial message
    welcome()
    print("=" * 153)
    print("{:^160s}".format("BLOOD DONATION CAMP"))
    print("{:^160s}".format("MANAGEMENT SYSTEM"))
    print("{:^160s}".format("PROJECT"))
    print("{:^160s}".format("MADE BY: Group A"))
    print("=" * 153)
    print()
    
    
#Doner Management
def register_doner(name,gender,bgroup,contact,address,dofb):
    query = """INSERT INTO Donor (name, gender, blood_group, contact_number,address, dofb,age)
               VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (name, gender, bgroup, contact,address, dofb, calculate_age(dofb)))
    db.commit()
    print("Donor registered successfully!")
    
def search_doner(name=None,did=None):
    if name:
        cursor.execute("SELECT * FROM Donor WHERE name = %s", (name,))
    elif did:
        cursor.execute("SELECT * FROM Donor WHERE donor_id = %s", (did,))
    else:
        return None

    donor = cursor.fetchone()
    if donor:
        return donor
    else:
        return donor

def update_doner_info(name=None,did=None):
    data = search_doner(name=name, did=did)
    if not data:
        print("No donor found with the given details.")
        return

    print("What would you like to update?")
    print("1. Name")
    print("2. Date of Birth")
    print("3. Gender")
    print("4. Blood Group")
    print("5. Contact Number")
    print("6. Address")
    
    choice_input = input("Enter your choices separated by commas (e.g., 1,3): ")
    try:
        choices = [int(choice.strip()) for choice in choice_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by commas.")
        return

    updates = {}
    if 1 in choices:
        updates['name'] = input("Enter the new NAME: ")
    if 2 in choices:
        updates['dofb'] = input("Enter the new DATE OF BIRTH (YYYY-MM-DD): ")
        updates['age'] = calculate_age(updates['dofb'])
    if 3 in choices:
        updates['gender'] = input("Enter the new GENDER (M/F): ")
    if 4 in choices:
        updates['blood_group'] = input("Enter the new BLOOD GROUP (e.g., A+, O-): ")
    if 5 in choices:
        updates['contact_number'] = input("Enter the new CONTACT NUMBER: ")
    if 6 in choices:
        updates['address'] = input("Enter the new ADDRESS: ")
    query_parts = []
    values = []
    for column, value in updates.items():
        query_parts.append(f"{column} = %s")
        values.append(value)
    if name:
        query = f"UPDATE Donor SET {', '.join(query_parts)} WHERE name = %s"
        values.append(name)
    elif did:
        query = f"UPDATE Donor SET {', '.join(query_parts)} WHERE donor_id = %s"
        values.append(did)

    
    cursor.execute(query, tuple(values))
    db.commit()
    print("Donor information updated successfully!")
 
#Camp Management
def register_camp():
    cdate = input("Enter CAMP DATE (YYYY-MM-DD): ")
    location = input("Enter CAMP LOCATION: ")
    organizer = input("Enter ORGANIZER NAME: ")

    query = """INSERT INTO Camp (cdate, location, organizer)
               VALUES (%s, %s, %s)"""
    cursor.execute(query, (cdate, location, organizer))
    db.commit()
    cursor.execute("SELECT camp_id FROM camp WHERE location = %s and cdate = %s", (location,cdate))
    cid=cursor.fetchone()
    print("Camp registered successfully with CAMP ID",cid[0])

def update_camp_info(camp_id=None, location=None):
    if camp_id:
        cursor.execute("SELECT * FROM camp WHERE camp_id = %s", (camp_id,))
    elif location:
        cursor.execute("SELECT * FROM camp WHERE location = %s", (location,))
    else:
        print("Please provide either camp_id or location to update camp information.")
        return

    data = cursor.fetchone()

    if data:
        print("\nCamp Found!")
        print("Current Camp Details:")
        print(f"Camp ID: {data[0]}, Date: {data[1]}, Location: {data[2]}, Organizer: {data[3]}")
        
        # Now ask which fields to update
        print("\nWhat would you like to update?")
        print("1. Date")
        print("2. Location")
        print("3. Organizer")
        choice = input("Enter the number(s) of the field(s) to update, separated by commas: ")

        # Update the selected fields
        if '1' in choice:
            new_date = input("Enter the new date of the camp (YYYY-MM-DD): ")
            cursor.execute("UPDATE camp SET cdate = %s WHERE camp_id = %s", (new_date, data[0]))
        if '2' in choice:
            new_location = input("Enter the new location of the camp: ")
            cursor.execute("UPDATE camp SET location = %s WHERE camp_id = %s", (new_location, data[0]))
        if '3' in choice:
            new_organizer = input("Enter the new organizer name: ")
            cursor.execute("UPDATE camp SET organizer = %s WHERE camp_id = %s", (new_organizer, data[0]))
        
        db.commit()
        print("\nCamp information updated successfully!")
    else:
        print("No camp found with the given details.")

def list_upcoming_camps():
    cursor.execute("SELECT * FROM Camp WHERE cdate > NOW()")
    camps = cursor.fetchall()
    return camps
#Donation Management
def manage_inventory_and_donation(donor_id, camp_id, blood_group, quantity, recipient_id=None):
    """
    Manages donation table and updates the inventory.
    Args:
        donor_id (int): ID of the donor.
        camp_id (int): ID of the camp where the donation happened.
        blood_group (str): Blood group of the donated blood.
        quantity (float): Quantity of blood donated (in liters).
        recipient_id (int, optional): ID of the recipient if blood is allocated directly.
    """
    try:
        # Add donation entry
        cursor.execute("""
        INSERT INTO donation (donor_id, camp_id, blood_group, quantity, recipient_id)
        VALUES (%s, %s, %s, %s, %s)
        """, (donor_id, camp_id, blood_group, quantity, recipient_id))
        donation_id = cursor.lastrowid  # Get the ID of the new donation entry
        print(f"Donation recorded successfully with Donation ID: {donation_id}")

        # Check if inventory already has this blood group
        cursor.execute("""
        SELECT inventory_id, quantity FROM inventory WHERE blood_group = %s
        """, (blood_group,))
        inventory_data = cursor.fetchone()

        # If blood group exists in inventory, update the quantity
        if inventory_data:
            inventory_id, existing_quantity = inventory_data
            new_quantity = existing_quantity + quantity
            cursor.execute("""
            UPDATE inventory SET quantity = %s WHERE inventory_id = %s
            """, (new_quantity, inventory_id))
            print(f"Inventory updated: {blood_group} now has {new_quantity} liters.")
        else:
            # If blood group doesn't exist, create a new inventory entry
            today = datetime.date.today()
            today_string = today.strftime("%Y-%m-%d")  # YYYY-MM-DD format
            expiration_date = calculate_date_after_n_days(today_string, 35)

            cursor.execute("""
            INSERT INTO inventory (blood_group, quantity, expiration_date, donation_id)
            VALUES (%s, %s, %s, %s)
            """, (blood_group, quantity, expiration_date, donation_id))
            print(f"New inventory entry created for blood group {blood_group} with {quantity} liters.")

        # Commit the changes to the database
        db.commit()
        print("Inventory and donation table updated successfully.")
    except mysql.connector.Error as err:
        db.rollback()
        print(f"Error: {err}")

def view_donation_history(donor_id=None, donor_name=None):
    # If donor_id is provided, fetch donation history based on donor_id
    if donor_id:
        cursor.execute("""
        SELECT donor.name, donor.blood_group, donor.contact_number, donation.donation_id, donation.camp_id, donation.blood_group AS donation_blood_group, donation.quantity, camp.cdate
        FROM donor
        JOIN donation ON donor.donor_id = donation.donor_id
        JOIN camp ON donation.camp_id = camp.camp_id
        WHERE donor.donor_id = %s
        ORDER BY camp.cdate DESC
        """, (donor_id,))
    # If donor_name is provided, fetch donation history based on donor_name
    elif donor_name:
        cursor.execute("""
        SELECT donor.name, donor.blood_group, donor.contact_number, donation.donation_id, donation.camp_id, donation.blood_group AS donation_blood_group, donation.quantity, camp.cdate
        FROM donor
        JOIN donation ON donor.donor_id = donation.donor_id
        JOIN camp ON donation.camp_id = camp.camp_id
        WHERE donor.name = %s
        ORDER BY camp.cdate DESC
        """, (donor_name,))
    else:
        print("Please provide either donor_id or donor_name to view donation history.")
        return

    # Fetch and display the results
    donations = cursor.fetchall()
    
    if donations:
        print("\nDonation History Report:")
        print(f"{'Donor Name':<20} {'Blood Group':<10} {'Contact Number':<20} {'Donation ID':<10} {'Camp ID':<10} {'Donation Blood Group':<20} {'Quantity':<10} {'Camp Date'}")
        print("="*90)
        
        for donation in donations:
            print(f"{donation[0]:<20} {donation[1]:<10} {donation[2]:<20} {donation[3]:<10} {donation[4]:<10} {donation[5]:<20} {donation[6]:<10} {donation[7]}")
    else:
        print("No donation history found for the specified donor.")

#Recipient Management
def register_recipient():
    hname = input("Enter HOSPITAL NAME: ")
    haddress = input("Enter HOSPITAL ADDRESS: ")
    hcontact = input("Enter HOSPITAL CONTACT: ")
    authorized_person = input("Enter AUTHORIZED PERSON NAME: ")

    query = """INSERT INTO Recipient (hname, haddress, hcontact_number, authorized_person)
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (hname, haddress, hcontact, authorized_person))
    db.commit()
    print("Recipient registered successfully!")

def search_recipient(name=None, recipient_id=None):
    if name:
        cursor.execute("SELECT * FROM recipient WHERE hname = %s", (name,))
    elif recipient_id:
        cursor.execute("SELECT * FROM recipient WHERE recipient_id = %s", (recipient_id,))
    else:
        print("Please provide either recipient name or recipient ID to search.")
        return
    
    data = cursor.fetchone()
    return data

def update_recipient_info(recipient_id=None, recipient_name=None):
    if not recipient_id and not recipient_name:
        print("Please provide either recipient ID or recipient name to update recipient information.")
        return

    # If recipient_id is provided, search by recipient_id
    if recipient_id:
        cursor.execute("SELECT * FROM recipient WHERE recipient_id = %s", (recipient_id,))
    # If recipient_name is provided, search by recipient_name
    elif recipient_name:
        cursor.execute("SELECT * FROM recipient WHERE hname = %s", (recipient_name,))

    # Fetch the recipient data
    recipient = cursor.fetchone()

    if recipient:
        print("\nCurrent Recipient Information:")
        print(f"ID: {recipient[0]}, Name: {recipient[1]}, Address: {recipient[2]}, Contact: {recipient[3]}, Authorized Person: {recipient[4]}")
        
        print("\nWhat would you like to update?")
        print("1. Hospital Name")
        print("2. Hospital Address")
        print("3. Hospital Contact Number")
        print("4. Authorized Person")
        choices = input("Enter the choice(s) to update (comma-separated for multiple): ").split(',')

        for choice in choices:
            if choice.strip() == '1':
                new_name = input("Enter new Hospital Name: ")
                cursor.execute("UPDATE recipient SET hname = %s WHERE recipient_id = %s", (new_name, recipient[0]))
            elif choice.strip() == '2':
                new_address = input("Enter new Hospital Address: ")
                cursor.execute("UPDATE recipient SET haddress = %s WHERE recipient_id = %s", (new_address, recipient[0]))
            elif choice.strip() == '3':
                new_contact = input("Enter new Hospital Contact Number: ")
                cursor.execute("UPDATE recipient SET hcontact_number = %s WHERE recipient_id = %s", (new_contact, recipient[0]))
            elif choice.strip() == '4':
                new_authorized_person = input("Enter new Authorized Person: ")
                cursor.execute("UPDATE recipient SET authorized_person = %s WHERE recipient_id = %s", (new_authorized_person, recipient[0]))
            else:
                print(f"Invalid choice: {choice.strip()}. No changes made.")
        
        db.commit()
        print("\nRecipient information updated successfully.")
    else:
        print("No recipient found with the provided ID or Name.")

def allocate_blood_to_recipient(blood_group, quantity_needed, recipient_id):
    """
    Allocates blood to a recipient based on blood group and updates the inventory and donation records.
    Args:
        blood_group (str): The blood group of the required blood.
        quantity_needed (float): Total quantity of blood needed (in liters).
        recipient_id (int): The recipient ID to allocate the blood to.
    """
    try:
        # Validate quantity_needed
        if quantity_needed % 0.5 != 0:
            print("Quantity needed must be in multiples of 0.5L (e.g., 0.5, 1.0, 1.5).")
            return

        # Fetch donations for the given blood group
        cursor.execute("""
        SELECT donation_id, quantity, recipient_id
        FROM donation
        WHERE blood_group = %s AND (recipient_id IS NULL OR recipient_id = 0)
        ORDER BY quantity DESC
        """, (blood_group,))
        donations = cursor.fetchall()

        if not donations:
            print(f"No available donations found for blood group: {blood_group}.")
            return

        total_allocated = 0.0
        for donation_id, donated_quantity, existing_recipient_id in donations:
            if total_allocated >= quantity_needed:
                break

            # Determine the amount to allocate from this donation
            allocation = min(quantity_needed - total_allocated, donated_quantity, 1.0)
            total_allocated += allocation

            # Update the recipient field in the donation table
            cursor.execute("""
            UPDATE donation
            SET recipient_id = %s, quantity = quantity - %s
            WHERE donation_id = %s
            """, (recipient_id, allocation, donation_id))

            # Update inventory for the specific blood group
            cursor.execute("""
            UPDATE inventory
            SET quantity = quantity - %s
            WHERE blood_group = %s
            """, (allocation, blood_group))

            print(f"Allocated {allocation}L of blood from Donation ID: {donation_id} to Recipient ID: {recipient_id}.")

        if total_allocated < quantity_needed:
            print(f"Only {total_allocated}L of blood could be allocated, which is less than the required {quantity_needed}L.")
        else:
            print(f"Successfully allocated {total_allocated}L of blood to Recipient ID: {recipient_id}.")

        # Commit the transaction
        db.commit()

    except mysql.connector.Error as err:
        db.rollback()
        print(f"Error: {err}")

if __name__=="__main__":
    intro()
    pwd='Mysql#123'#input('Enter the database password')
    db = mysql.connector.connect(host="localhost",user="root",password=pwd)
    cursor = db.cursor()
    create_tables(cursor)
    camps = list(list_upcoming_camps())
    if not camps:
        print("NOTE:- Please register camp first! ")
    while True:
        print("\n=== Main Menu ===")
        print("A. Camp management")
        print("B. Donor and Donation management")
        print("C. Recipient management")
        print("0. Exit\n\n")
        time.sleep(2)
        
        choice = input("Enter your choice (A,B,C,0): ")
        if choice.lower()=="b":
            while True:
                print("\n=== Donor and Donation Management ===")
                print("1. To Register Donor and their donation")
                print("2. To Search Donor by Name or by ID")
                print("3. To Update Donor Information")
                print("4. To list all donors")
                print("5. To Delete Donor")
                print("0. Back to main menu\n")
                time.sleep(2)
                choice = input("Enter your choice (1,2,3,4,5,0): ")
                if choice == '1':
                    camp_id=input("Enter CAMP ID of the camp: ")
                    while True:
                        name = input("Enter NAME: ").title()
                        gender = input("Enter GENDER (M/F): ").upper()
                        bgroup = input("Enter BLOOD GROUP (e.g., A+, O-): ").capitalize()
                        contact = input("Enter CONTACT NUMBER: ")
                        address = input("Enter ADDRESS: ").title()
                        dofb = input("Enter DATE OF BIRTH (YYYY-MM-DD): ")
                        quantity=input("Enter Quantity (in liters, e.g., 0.5, 1.0): ")
                        
                        register_doner(name,gender,bgroup,contact,address,dofb)
                        cursor.execute("select donor_id from donor where name=%s and dofb=%s and blood_group=%s",(name,dofb,bgroup))
                        data=cursor.fetchone()
                        manage_inventory_and_donation(data[0], camp_id, bgroup, quantity)
                        if input("Is there more doners?(y/n): ").lower()!="y":
                            break
                elif choice == '2':
                    name = input("Enter the donor name to search (or leave blank to search by ID): ")
                    if not name:
                        did = input("Enter the donor ID to search: ")
                        donor =search_doner(did=int(did))
                    else:
                        donor =search_doner(name=name)
                    if donor:
                                print("Donor id =",data[0])
                                print("Name =",data[1])
                                print("Date of brith =",data[2])
                                print("Age =",data[3])
                                print("Gender =",data[4])
                                print("Blood Group =",data[5])
                                print("Contact No. =",data[6])
                                print("Address =",data[7])
                    else:
                        print("No donor found!!! ")
                
                elif choice == '3':
                    print("Update donor information:")
                    name = input("Enter the donor name to update (or leave blank to search by ID): ")
                    if not name:
                        did = input("Enter the donor ID to update: ")
                        update_doner_info(did=int(did))
                    else:
                        update_doner_info(name=name)
                        
                elif choice == '4':
                    cursor.execute("select * from donor")
                    datas=cursor.fetchall()
                    if datas:
                        for data in range(len(datas)):
                            datas[data]=list(datas[data])
                            datas[data][0]=str(datas[data][0])
                            datas[data][3]=str(datas[data][3])
                            datas[data][2]=datetime.date.isoformat(datas[data][2])
                        a=cuteprint([["DONOR ID","NAME","DATE OF BRITH","AGE","GENDER","BLOOD GROUP","CONTACT NO.","ADDRESS"]]+datas,0)
                        for i in a:
                            for j in i:
                                print(j,end="")
                    else:
                        print("No donor")
                        
                elif choice == '5':
                    name = input("Enter the donor name to delete (or leave blank to search by ID): ")
                    if not name:
                        did = input("Enter the donor ID to delete: ")
                        donor =search_doner(did=int(did))
                    else:
                        donor =search_doner(name=name)
                    if donor:
                        cursor.execute("delete from donor where donor_id=%s",(did,))
                        print("Donor deleted sucessfully!!")
                    else:
                        print("No donor found!!")
                        
                elif choice == '0':
                    break
                
                else:
                    print("Invalid choice! Please enter a valid option.")

        elif choice.lower()=="a":
            while True:
                print("\n=== Camp Management ===")
                print("1. To Register Camp")
                print("2. To List Upcomimg Camp ")
                print("3. To Cancel camp")
                print("0. Back to main menu\n")
                time.sleep(2)
                choice = input("Enter your choice (1,2,3,0): ")
                if choice == '1':   
                    register_camp()
                elif choice == '2':
                    camps = list(list_upcoming_camps())
                    if camps:
                        for camp in range(len(camps)):
                            camps[camp]=list(camps[camp])
                            camps[camp][0]=str(camps[camp][0])
                            camps[camp][1]=datetime.date.isoformat(camps[camp][1])
                        a=cuteprint([["CAMP ID","DATE","LOCATION","ORGANIZER"]]+camps,0)
                        for i in a:
                            for j in i:
                                print(j,end="")
                    else:
                        print("No camps yet!")
                elif choice == '3':
                    cid=int(input("Enter the CAMP ID of the camp to cancel it: "))
                    cursor.execute("select cdate from camp where camp_id=%s",(cid,))
                    cdate=cursor.fetchone()
                    if cdate:
                        if datediff(datetime.date.isoformat(cdate[0]))>2:
                            cursor.execute("delete from camp where camp_id=%s",(cid,))
                            print("Camp canceled sucessfully!!")
                        else:
                            print('Sorry, camp can not be canceled before two days')
                    else:
                        print("No camp found!!")
                elif choice == '0':
                    break
                else:
                    print("Invalid choice! Please enter a valid option.")

        elif choice.lower()=="c":
            while True:
                print("\n=== Recipient Management ===")
                print("1. To Register Recipient")
                print("2. To Search Recipent by Name or by ID")
                print("3. To Update Recipient Information")
                print("4. To Show All Recipients")
                print("5. To Allocate Donation")
                print("0. Back to main menu\n  ")
                time.sleep(2)
                choice = input("Enter your choice (1,2,3,4,5,0): ")
                if choice == '1':   
                    register_recipient()
                elif choice == '2':
                    name = input("Enter the recipient name to search (or leave blank to search by ID): ")
                    if not name:
                        recipient_id = input("Enter the recipient ID to search: ")
                        recipient =search_recipient(recipient_id=int(recipient_id))
                    else:
                        recipient =search_recipient(name=name)
                    if recipient:
                        data=recipient
                        if data:
                            print("\nRecipient Information:")
                            print(f"Recipient ID: {data[0]}")
                            print(f"Hospital Name: {data[1]}")
                            print(f"Hospital Address: {data[2]}")
                            print(f"Contact Number: {data[3]}")
                            print(f"Authorized Person: {data[4]}")
                        else:
                            print("No recipient found with the provided details.")
                
                elif choice == '3':
                    name = input("Enter the recipient name to update (or leave blank to search by ID): ")
                    if not name:
                        recipient_id = input("Enter the recipient ID to search: ")
                        update_recipient_info(recipient_id=int(recipient_id))
                    else:
                        update_recipient_info(recipient_name=name)
                        
                elif choice == '4':
                    cursor.execute("select * from recipient")
                    datas=cursor.fetchall()
                    if datas:
                        for data in range(len(datas)):
                            datas[data]=list(datas[data])
                            datas[data][0]=str(datas[data][0])                 
                        a=cuteprint([["RECIPIENT ID","HOSPITAL NAME","HOSPITAL ADDRESS","CONTACT NO.","AUTHORIZED PERSON NAME"]]+datas,0)
                        for i in a:
                            for j in i:
                                print(j,end="")
                    else:
                        print("No recipient")
                        
                elif choice == '5':
                    name = input("Enter the Hospital name to search (or leave blank to search by ID): ")
                    if not name:
                        recipient_id = input("Enter the recipient ID to search: ")
                        recipient =search_recipient(recipient_id=int(recipient_id))
                    else:
                        recipient =search_recipient(name=name)
                        if recipient:
                            recipient_id=cursor.fetchone(cursor.execute("select recipient_id from recipient where name=%s",(name,)))[0]
                            
                    if recipient:
                        blood_group = input("Enter Blood Group: ").capitalize()
                        quantity_needed = float(input("Enter Quantity Needed (in liters, e.g., 0.5, 1.0): "))
                        allocate_blood_to_recipient(blood_group, quantity_needed, recipient_id)
                    else:
                        print("No recipient found!!! ")
                    
                elif choice == '0':
                    break
                else:
                    print("Invalid choice! Please enter a valid option.")
        
        elif choice=='0' or choice.lower()=='o':
            print("Exiting the system...")
            db.close()
            break