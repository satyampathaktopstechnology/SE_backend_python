import sqlite3

print("Program start")

con = sqlite3.connect("student.db")

cursor = con.cursor()




# cursor.execute("create table student (id int primary key,name varchar(50),age int,address varchar(50))")

# cursor.execute("insert into student values(1,'Satyam',24,'Darbar')")
# cursor.execute("insert into student values(2,'Ashish',22,'Kim')")
# cursor.execute("insert into student values(3,'Rajesh',22,'kolapur')")
# cursor.execute("insert into student values(4,'Chetan',25,'Surat')")
# cursor.execute("insert into student values(5,'Jagsih',30,'Bharuch')")

# con.commit()

cursor.execute("select * from student")

rows = cursor.fetchall()

print("Student Record")
for i in rows:
    print(i)

con.close()
print("Program ended")

