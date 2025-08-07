import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__)
DATABASE = 'database.db'

# --- Database Connection Code ---
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# --- Login Page Route ---
@app.route("/", methods=['GET', 'POST'])
def login():
    # This part runs when you click the "Login" button
    if request.method == 'POST':
        db = get_db()
        username = request.form['username']
        password = request.form['password']

        # SECURE VERSION: Using Parameterized Queries
        # The '?' placeholders keep user data separate from the SQL command.
        # This makes injection impossible.
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor = db.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            return "<h1>Login Successful! Welcome.</h1>"
        else:
            return "<h1>Login Failed. Invalid credentials.</h1>"

    # This just shows the login page
    return render_template("login.html")

# --- Function to create the database for the first time ---
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == "__main__":
    app.run(debug=True)