-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

-- Create the cities table
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Populate the states table
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas'), ('New York'), ('Nevada');

-- Populate the cities table
INSERT INTO cities (name, state_id) VALUES 
('San Francisco', 1), 
('San Jose', 1), 
('Los Angeles', 1), 
('Fremont', 1), 
('Livermore', 1), 
('Page', 2), 
('Phoenix', 2), 
('Dallas', 3), 
('Houston', 3), 
('Austin', 3), 
('New York', 4), 
('Las Vegas', 5), 
('Reno', 5), 
('Henderson', 5), 
('Carson City', 5);

-- Select all data from states and cities tables to verify insertion
SELECT * FROM states;
SELECT * FROM cities;
