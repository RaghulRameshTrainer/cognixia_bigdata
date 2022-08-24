import sqlite3

dbh=sqlite3.connect('cognixia.db')
c=dbh.cursor()
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS employee( empname TEXT, tech TEXT, exp TEXT)")
def load_data():
    #c.execute("INSERT INTO employee VALUES('Raghul Ramesh','Python',17)")
    #c.execute("INSERT INTO employee VALUES('Kathir V','Hadoop',10)")
    e_name=input("Enter your name:")
    e_tech=input("Enter your skill:")
    e_exp=input("Enter your experience:")
    c.execute("INSERT INTO employee VALUES(?,?,?)",(e_name,e_tech,e_exp))
    dbh.commit()
def update_data():
    c.execute("UPDATE employee SET tech='Perl' , exp='12' WHERE empname='Vijay'")
    dbh.commit()
    c.close()
    dbh.close()
def delete_data():
    c.execute("DELETE FROM employee WHERE empname='Venkatesh'")
    dbh.commit()
    c.close()
    dbh.close()
def fetch_data():
    c.execute("SELECT * FROM employee")
    """
    fetchone
    fetchmany
    fetchall
    """
    #print(c.fetchone())
    #print(c.fetchmany(5))
    for row in c.fetchall():
        if row[0] != '':
            print(row[0]+' --> '+   row[1] + ' ---> ' + str(row[-1]))
    # print(c.fetchall())
#create_table()
# for x in range(5):
#     load_data()
# c.close()
# dbh.close()

#update_data()
#delete_data()
fetch_data()