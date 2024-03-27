
# 0x0D. SQL - Introduction

# MySQL Database Management Scripts

This repository contains a collection of SQL scripts for managing databases and tables within a MySQL server. These scripts are designed to perform a variety of tasks, including database creation, table manipulation, data insertion, and complex querying to facilitate database management and data analysis.

## Table of Contents

- [Scripts Description](#scripts-description)
- [Usage](#usage)

## Scripts Description

Each script in this repository serves a specific purpose:

- `0-list_databases.sql`: Lists all databases on the MySQL server.
- `1-create_database_if_missing.sql`: Creates the database `hbtn_0c_0` if it doesn't already exist.
- `2-remove_database.sql`: Removes the database `hbtn_0c_0` if it exists.
- `3-list_tables.sql`: Lists all tables within the current database.
- `4-first_table.sql`: Creates a table named `first_table` with columns `id` and `name`.
- `5-full_table.sql`: Shows the full description of `first_table`.
- `6-list_values.sql`: Lists all rows within `first_table`.
- `7-insert_value.sql`: Inserts a row with id `89` and name `"Best School"` into `first_table`.
- `8-count_89.sql`: Counts the number of records in `first_table` with an `id` of `89`.
- `9-full_creation.sql`: Creates and populates `second_table` with multiple rows.
- `10-top_score.sql`: Lists all records from `second_table` ordered by descending score.
- `11-best_score.sql`: Lists records from `second_table` with a score of at least `10`, ordered by descending score.
- `12-no_cheating.sql`: Updates the score for "Bob" in `second_table` to `10`.
- `13-change_class.sql`: Removes records from `second_table` with a score of `5` or less.
- `14-average.sql`: Calculates the average score of all records in `second_table`.
- `15-groups.sql`: Lists the number of records sharing the same score in `second_table`, ordered by descending count.
- `16-no_link.sql`: Lists all records in `second_table` with a non-empty name, ordered by descending score.
- `100-move_to_utf8.sql`: Converts `first_table` in the database `hbtn_0c_0` to use UTF8 encoding.

## Usage

To execute any of these scripts, use the MySQL command line interface or a MySQL client, and run: