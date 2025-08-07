-- Delete the table if it already exists to start fresh
DROP TABLE IF EXISTS users;

-- Create a new table to store users
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

-- Add a sample user so we can log in
INSERT INTO users (username, password) VALUES ('admin', 'password123');