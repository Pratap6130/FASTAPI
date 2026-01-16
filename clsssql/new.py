# import mysql.connector as sql
# conn = sql.connect(
#     host="localhost",
#     user="root",
#     password="Password")

# conn.autocommit =  True
# cur = conn.cursor()
# cur.execute("CREATE DATABASE IF NOT EXISTS newData;")
# cur.execute("USE newData;")
# cur.execute("create table if not exists student(roll int, name varchar(20), per float);")
# cur.execute("insert into student values(1, 'Alice', 85.5);")
# cur.close()
# conn.close()


# import mysql.connector as sql
# conn = sql.connect(
#     host="localhost",
#     user="root",
#     password="Password")

# conn.autocommit =  True

# cur = conn.cursor()
# cur.execute("CREATE DATABASE IF NOT EXISTS newData;")
# cur.execute("USE newData;")
# cur.execute("create table if not exists student(roll int, name varchar(20), per float);")

# roll = int(input("Enter roll number: "))
# name = input("Enter name: ")
# per = float(input("Enter percentage: "))

# query = f"insert into student values({roll}, '{name}', {per});"

# cur.execute(query)

# cur.close()
# conn.close()



# import mysql.connector as sql

# conn = sql.connect( host="localhost", user="root", password="Password")

# conn.autocommit =  True

# cur = conn.cursor()
# cur.execute("CREATE DATABASE IF NOT EXISTS newData;")
# cur.execute("USE newData;")
# cur.execute("create table if not exists student(roll int, name varchar(20), per float);")

# while True:
#     roll = int(input("Enter roll number: "))
#     name = input("Enter name: ")
#     per = float(input("Enter percentage: "))
#     query = f"insert into student values({roll}, '{name}', {per});"
#     cur.execute(query)

#     n = input(" you want to enter more records(Y/N):")
#     if n== 'N' or n== 'n':
#         break

# cur.close()
# conn.close()




# import mysql.connector as sql
# conn = sql.connect( host="localhost", user="root", password="Password")
# conn.autocommit =  True

# cur = conn.cursor()
# cur.execute("use newData;")
# cur.execute("select * from student;")

# data = cur.fetchone()
# print(data)

# data = cur.fetchone()
# print(data)

# data = cur.fetchone()
# print(data)

# data = cur.fetchone()
# print(data)

# cur.close()
# conn.close()




# import mysql.connector as sql
# conn = sql.connect( host="localhost", user="root", password="Password")
# conn.autocommit =  True

# cur = conn.cursor()
# cur.execute("use newData;")
# cur.execute("select * from student;")

# while True:
#     data = cur.fetchone()
#     if data == None:
#         break
#     print(data)

# cur.close()
# conn.close()


# import mysql.connector as sql
# conn = sql.connect( host="localhost", user="root", password="Password")
# conn.autocommit =  True

# cur = conn.cursor()
# cur.execute("use newData;")
# cur.execute("select * from student;")

# data = cur.fetchmany(10)
# #print(data)
# for i in data:
#     print(i)

# #cur.close()
# conn.close()



# import mysql.connector as sql
# conn = sql.connect( host="localhost", user="root", password="Password")
# conn.autocommit =  True

# cur = conn.cursor()
# cur.execute("use newData;")
# cur.execute("select * from student;")

# data = cur.fetchall()
# print(data)

# #cur.close()
# conn.close()




import mysql.connector as sql
conn = sql.connect( host="localhost",
                    user="root",
                    password="Password")

conn.autocommit =  True

cur = conn.cursor()
cur.execute("use newData;")

query = "insert into student values(%s, %s, %s);"
data = [(105, "Suresh", 78.5),
        (106, "Ramesh", 88.5),
        (107, "Mahesh", 98.5)]

cur.executemany(query, data);

cur.fetchall()
cur.close()
conn.close()