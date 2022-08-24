import sqlite3

dbh=sqlite3.connect('cognixia.db')
c=dbh.cursor()
def create_table():
    c.execute("CREATE TABLE employee( empname TEXT, tech TEXT, exp TEXT)")
def load_data():
    #c.execute("INSERT INTO employee VALUES('Raghul Ramesh','Python',17)")
    #c.execute("INSERT INTO employee VALUES('Kathir V','Hadoop',10)")
    e_name=input("Enter your name:")
    e_tech=input("Enter your skill:")
    e_exp=input("Enter your experience:")
    c.execute("INSERT INTO employee VALUES(?,?,?)",(e_name,e_tech,e_exp))
    dbh.commit()

#create_table()
for x in range(5):
    load_data()
c.close()
dbh.close()