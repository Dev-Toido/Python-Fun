def create_tables():
    import mysql.connector as sql
    con = sql.connect(host="localhost", user="root", password="Mysql#123")
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS SMS;")
    cur.execute("USE SMS;")
    cur.execute("""CREATE TABLE IF NOT EXISTS S_D(
                S_ROLL INT PRIMARY KEY AUTO_INCREMENT,
                NAME VARCHAR(50), 
                STATUS VARCHAR(10) DEFAULT '',
                CONTDES VARCHAR(15));""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS T_D(
                TEST_NO INT PRIMARY KEY AUTO_INCREMENT,
                FM INT);""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS ANALYSIS(
                S_ROLL INT,
                FM INT DEFAULT 0,
                TM INT DEFAULT 0,
                PAGE FLOAT DEFAULT 0,
                PRIMARY KEY (S_ROLL),
                FOREIGN KEY (S_ROLL) REFERENCES S_D(S_ROLL)
                );""")
    con.commit()
    cur.close()
    print("Done")

create_tables()