# 0x0F. Python - Object-Relational Mapping

## This repository contains projects and tasks focused on Object-Relational Mapping (ORM) using Python. The primary objective is to learn and practice integrating Python with relational databases using the ORM paradigm, specifically leveraging SQLAlchemy, a powerful Python SQL toolkit and Object-Relational Mapping (ORM) library.

# Project Overview
The projects cover the following topics:

Connecting to MySQL with MySQLdb
Running SQL queries using Python scripts
Creating and manipulating database tables using SQLAlchemy
Working with relationships and advanced queries
Each task builds upon the previous one, gradually increasing in complexity and covering different aspects of ORM in Python.

# Project Structure

## The project structure is as follows:

0-select_states.py: Lists all states from the database.
1-filter_states.py: Lists all states with names starting with 'N'.
2-my_filter_states.py: Takes a user input and filters states accordingly.
3-my_safe_filter_states.py: Secure filtering against SQL injections.
4-cities_by_state.py: Lists all cities by state.
5-filter_cities.py: Similar to 4-cities_by_state.py but taking state as an argument.
6-model_state.py: Creates a State class using SQLAlchemy.
7-model_state_fetch_all.py: Fetches all State objects from the database.
8-model_state_fetch_first.py: Fetches the first State object from the database.
9-model_state_filter_a.py: Lists all State objects containing the letter 'a'.
10-model_state_my_get.py: Fetches a State object based on name.
11-model_state_insert.py: Inserts a new State object.
12-model_state_update_id_2.py: Updates the name of the state with ID=2.
13-model_state_delete_a.py: Deletes State objects containing 'a'.
14-model_city_fetch_by_state.py: Lists all City objects by state.
100-relationship_states_cities.py: Demonstrates a relationship between State and City.
101-relationship_states_cities_list.py: Lists all states and corresponding cities using relationships.
102-relationship_cities_states_list.py: Lists all cities and corresponding states using relationships.
model_city.py: Contains the City class.
model_state.py: Contains the State class.
relationship_city.py: Contains the City class using a relationship.
relationship_state.py: Contains the State class using a relationship.

# How to Run
- Setup:
Make sure to have a MySQL server running locally.
Create necessary databases and tables using the provided .sql files.
- Execution:
Each script is a standalone executable Python script.
Use chmod +x script_name.py to make the scripts executable.
Run the scripts with ./script_name.py followed by necessary arguments.
- Testing:
The .sql files contain sample data for testing purposes.
Use the provided test cases to verify functionality.
