import mysql.connector
import cv2
import pandas as pd

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="dhanush",
  password="abc12345"
)


mycursor = mydb.cursor()

# # mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("use med_hist")
# # mycursor.execute(select * from med_info)
# mycursor.execute("select P_id from med_info")
# myresult = mycursor.fetchall()
# last=(max(myresult))
# print(last[0])
# name = 'abhi'
# F_name = "kldsjafj"
# Address = "uhadsi"
# Adhaar = "56565"

# query="insert into med_info (name, F_name, Address, Adhaar, mob, alt_mob, email, DOB, Gender ) values ('Abhi Kumar Singh', 'Kartik Kumar Singh', 'Patna Bihar', 954178863049, 7352283805, 8935905626, 'abhi24680@outlook.com', '2001-09-12', 'M')"
# query=("insert into med_info (name, F_name, Address, Adhaar) values (%s, %s, %s, %s)")
# mycursor.execute(query,(name,F_name,Address, Adhaar))
# mydb.commit()
# print(mycursor.lastrowid)
# last= mycursor.insert_id() 
# print(last)
# mycursor.execute("select P_id from med_info where P_id = last_insert_id()")
# myresult = mycursor.fetchall()
# print(myresult)
# print("1 record inserted, id:",mycursor.lastrowid)
result="1.jpg"
x=result.split(".")
# print(x[0])
min = (x[0])
sql = ("SELECT * FROM Med_info where P_id = %s;")
mycursor = mydb.cursor()
mycursor.execute(sql, (min,))
myresult = mycursor.fetchall()
df = pd.DataFrame()
for x in myresult:
  print(myresult)
  # df2 = pd.DataFrame(list(x)).T
  # df = pd.concat([df,df2])