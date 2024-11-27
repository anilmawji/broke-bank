import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="apple",
  database="banking_platform"
)

mycursor = mydb.cursor()

user_input = "janesmith@email.com' OR 1=1 -- "

query = f"SELECT * FROM users WHERE email_address = '{user_input}'"
mycursor.execute(query)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)