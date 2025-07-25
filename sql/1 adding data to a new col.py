


# Use the psycopg2 package to connect to the PostgreSQL server from Python. Call the connect() function of the psycopg2 module to connect to the PostgreSQL server.


"""
In this article, we are going to see how to Inserting data into a new column of an already existing table in MySQL using Python. Python allows the integration of a wide range of database servers with applications. A database interface is required to access a database from Python. MySQL Connector Python module is an API in python for communicating with a MySQL database.

Database table in use:


We are going to use geeks(Database name) database and table describing the salary.

Approach:

Import module.
Make a connection request with the database.
Create an object for the database cursor.
Execute the following MySQL query:

ALTER TABLE person
ADD salary int(20);
UPDATE persons SET salary = '145000' where Emp_Id=12;

And print the result.
Before starting let do the same in SQL:

Step 1: Create a new column with alter command.

ALTER TABLE table_name ADD column_name datatype;
-------------------------------------------
create table sport_interest_bak (
id int ,
sport_interest varchar(50));

update sport_interest set sport_interest = 'cricket' where id=7;
update sport_interest set sport_interest = 'football' where id=8;

update sport_interest s
inner join sport_interest_bak sb on s.id=sb.id
set s.sport_interest=sb.sport_interest;


"""


# Establish connection to MySQL database
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="geeks"
)

# getting the cursor by cursor() method
mycursor = db.cursor()
query_1 = "ALTER TABLE person ADD salary int(20);"
query_2 = "UPDATE persons SET salary = '145000' where Emp_Id=12;"

# execute the queries
mycursor.execute(query_1)
mycursor.execute(query_2)

mycursor.execute("select * from persons;")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

db.commit()

# close the Connection
db.close()











