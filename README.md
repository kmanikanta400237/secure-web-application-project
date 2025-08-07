# Create and Secure a Vulnerable Web Application

## Project Objective

This project demonstrates a common web vulnerability, **SQL Injection (SQLi)**, in a simple Python Flask application. The goal is to showcase the ability to identify, exploit, and then remediate a critical security flaw based on the OWASP Top 10. This project covers both offensive (red team) and defensive (blue team) security principles.

---

## Technology Stack

* **Backend:** Python, Flask
* **Database:** SQLite
* **Frontend:** HTML

---

## Setup and Usage

1.  Clone the repository: `git clone <your-repo-link>`
2.  Create and activate a virtual environment:
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  Install the required packages: `pip install -r requirements.txt`
4.  Initialize the database (run this once): `python -c "from app import init_db; init_db()"`
5.  Run the application: `flask run`
<img width="1920" height="1080" alt="exploit" src="https://github.com/user-attachments/assets/322660a4-531f-4f3a-a118-3ce84a576446" />

---

## Security Analysis: SQL Injection (SQLi)

### The Vulnerability

The application's login form was initially built using an unsafe SQL query that directly concatenated user input. This allowed an attacker to manipulate the query's logic and bypass authentication.

**Vulnerable Code (`app.py`):**
```python
# VULNERABILITY: SQL INJECTION
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor = db.execute(query)

The Exploit
An attacker can bypass the login without a password by providing a specially crafted username that comments out the rest of the SQL query.

Username: admin' --

Password: (leave blank)

The -- acts as a comment in SQL, causing the database to ignore the password check, find the user 'admin', and grant access.

The Fix (Remediation)
The vulnerability was fixed by using parameterized queries. This practice separates the SQL command from the user data, ensuring that user input is always treated as simple data and never as executable code.

Secure Code (app.py):

Python

# SECURE VERSION: Using Parameterized Queries
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor = db.execute(query, (username, password))<img width="1920" height="1080" alt="secure" src="https://github.com/user-attachments/assets/68cbc567-9c05-45f3-b3b2-799120b2f846" />

What I Learned
Hands-on experience with the #1 OWASP Top 10 vulnerability.

Practical application of both offensive techniques (exploiting the flaw) and defensive secure coding practices (remediating the flaw).

Reinforced the core security principle of "Never Trust User Input."

Experience with setting up and running a full-stack Python Flask application with a database.
