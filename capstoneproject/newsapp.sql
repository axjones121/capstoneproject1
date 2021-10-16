-- from the terminal run:
-- psql < newsapp.sql
DROP DATABASE IF EXISTS newsapp_capstone;

CREATE DATABASE newsapp_capstone;

\c newsapp_capstone

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(25) UNIQUE NOT NULL,
    password VARCHAR(70) NOT NULL
    
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    comment TEXT
);


INSERT INTO users
  (username, password)
VALUES
  ('dokie2027', 'j123lj4123jk4j123kj41k23j4');  
  -- rememeber to put in the semicolons
  

INSERT INTO comments 
( user_id, comment )
VALUES
    (1, 'Nice article');


-- refer to 24.4.8