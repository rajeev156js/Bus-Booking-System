import sqlite3
con=sqlite3.Connection("database")
cur=con.cursor()
try:
    cur.execute('create table operator(op_id numeric,name varchar(25),address varchar(25),phone numeric,email varchar(100))')
    cur.execute('create table route(route_id numeric,station_id numeric,station_name varchar(25))')

    cur.execute('create table bus(bus_id numeric,bus_type varchar(15),capacity numeric,fare numeric,r_id numeric,operator_id numeric,foreign key(r_id) references route(route_id) on delete cascade,foreign key(operator_id) references operator(op_id) on delete cascade)')

    cur.execute('create table run(b_id numeric,running_date date,seat_available numeric)')

    cur.execute('create table booking_history(booking_id numeric,p_name numeric,phone numeric,travel_on date,booked_on date,gender varchar(10),age numeric,source varchar(50),destination varchar(50),fare numeric,seats numeric)')
except:m=0
 
cur.execute("""INSERT INTO operator VALUES (101 , "Kamla" , "AB  road Guan" , 12345 , "Kamlabus@gmail.com")""")
cur.execute("""INSERT INTO  operator values(102 , "Rayeen" , "AB  road Guan" , 12346 , "rayeen@gmail.com" )""")
cur.execute("""INSERT INTO operator values(103 , "Kalyani" , "Hauj Khas Delhi" , 12347 , "Kalyani@gmail.com")""")
cur.execute("""INSERT INTO operator values(104 , "Mahakaal" ,"AB  road jhansi", 12348 , "mahakaal@gmail.com")""")

cur.execute("""INSERT INTO run    VALUES(201,"01/12/2022",30)""")
cur.execute("""INSERT INTO run    values(201,"02/12/2022",30)""")
cur.execute("""INSERT INTO run    values(201,"03/12/2022",30)""")
cur.execute("""INSERT INTO run    values(201,"04/12/2022",30)""")
cur.execute("""INSERT INTO run    values(202,"01/12/2022",30)""")
cur.execute("""INSERT INTO run    values(202,"02/12/2022",30)""")
cur.execute("""INSERT INTO run    values(202,"03/12/2022",30)""")
cur.execute("""INSERT INTO run    values(202,"04/12/2022",30)""")
cur.execute("""INSERT INTO run    values(203,"01/12/2022",30)""")
cur.execute("""INSERT INTO run    values(203,"02/12/2022",30)""")
cur.execute("""INSERT INTO run    values(203,"03/12/2022",30)""")
cur.execute("""INSERT INTO run    values(203,"04/12/2022",30)""")
cur.execute("""INSERT INTO run    values(204,"01/12/2022",30)""")
cur.execute("""INSERT INTO run    values(204,"02/12/2022",30)""")
cur.execute("""INSERT INTO run    values(204,"03/12/2022",30)""")
cur.execute("""INSERT INTO run    values(204,"04/12/2022",30)""")


cur.execute("""INSERT INTO route  VALUES(1,1001,"Guna")""")
cur.execute("""INSERT INTO route  values(1,1002,"JP College")""")
cur.execute("""INSERT INTO route  values(1,1003,"Binagunj")""")
cur.execute("""INSERT INTO route  values(1,1004,"Biora")""")
cur.execute("""INSERT INTO route  values(1,1005,"Bhopal")""")

cur.execute("""INSERT INTO route  values(2,2001,"Bhopal")""")
cur.execute("""INSERT INTO route  values(2,2002,"Biora")""")
cur.execute("""INSERT INTO route  values(2,2003,"Binagunj")""")
cur.execute("""INSERT INTO route  values(2,2004,"JP College")""")
cur.execute("""INSERT INTO route  values(2,2005,"Guna")""")

cur.execute("""INSERT INTO route   VALUES (3 , 3001 , "Delhi")""")
cur.execute("""INSERT INTO route   VALUES (3 , 3002 , "Agra")""")
cur.execute("""INSERT INTO route   VALUES (3 , 3003 , "Jhasi")""")
cur.execute("""INSERT INTO route   VALUES (3 , 3004 , "Shivpuri")""")
cur.execute("""INSERT INTO route   VALUES (3 , 3005 , "Guna")""")

##cur.execute("""INSERT INTO route   VALUES (3 , 6 , "JP College")""")
##cur.execute("""INSERT INTO route   VALUES (3 , 7 , "Binaganj")""")
##cur.execute("""INSERT INTO route   VALUES (3 , 8 , "Biora")""")
##cur.execute("""INSERT INTO route   VALUES (3 , 9 , "Bhopal")""")

##cur.execute("""INSERT INTO route   VALUES (4 , 1 , "Bhopal")""")
##cur.execute("""INSERT INTO route   VALUES (4 , 2 , "Biora")""")
##cur.execute("""INSERT INTO route   VALUES (4 , 3 , "Binaganj")""")
##cur.execute("""INSERT INTO route   VALUES (4 , 4 , "JP college")""")

cur.execute("""INSERT INTO route   VALUES (4 , 4001 , "Guna")""")
cur.execute("""INSERT INTO route   VALUES (4 , 4002 , "Shivpuri")""")
cur.execute("""INSERT INTO route   VALUES (4 , 4003 , "Jhansi")""")
cur.execute("""INSERT INTO route   VALUES (4 , 4004 , "Agra")""")
cur.execute("""INSERT INTO route   VALUES (4 , 4005 , "Delhi")""")


cur.execute("""INSERT INTO BUS  VALUES (201 , "AC 2x2" , 40 , 1000 , 1 ,101)""")
cur.execute("""INSERT INTO  BUS  values(202 , "AC 3x2" , 50 , 800 , 2 ,102)""")
cur.execute("""INSERT INTO BUS  values(201 , "NON AC 2x2" , 40 , 600 , 1 ,101)""")
cur.execute("""INSERT INTO BUS  values(202 , "NON AC 3x2" , 40 , 600 , 2 ,102)""")

 

cur.execute('select * from booking_history')
a=cur.fetchall()
print(a)

"""
CREATE TABLE Enroll (sno INT,cno INT,jdate date, PRIMARY KEY(sno,cno),
FOREIGN KEY(sno) REFERENCES Student(sno) ON DELETE CASCADE, 
FOREIGN KEY(cno) REFERENCES Course(cno) ON DELETE CASCADE);
"""

con.commit()
con.close()
