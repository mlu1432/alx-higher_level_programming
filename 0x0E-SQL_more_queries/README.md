# 0x0E-SQL More Queries


## Overview

This project aims to deepen understanding of SQL, focusing on more complex queries involving multiple tables, sub-queries, JOIN operations, and the manipulation of privileges. It covers various SQL concepts including user creation and rights management, table creation with constraints, and querying data from related tables.

## Files and Descriptions

### Privileges

- `0-privileges.sql`: Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2`.

### User Creation

- `1-create_user.sql`: Script to create the MySQL server user `user_0d_1` with all privileges and a password.
- `2-create_read_user.sql`: Script to create a user with only SELECT privileges.

### Table Creation and Constraints

- `3-force_name.sql`: Creates a table that forces a non-NULL name field.
- `4-never_empty.sql`: Ensures a table's name field can never be empty.
- `5-unique_id.sql`: Creates a table with a unique ID.

### Data Manipulation

- `6-states.sql`: Inserts data into the states table.
- `7-cities.sql`: Inserts data into the cities table.

### Querying Data

- `8-cities_of_california_sub-query.sql`: Lists all cities of California using a sub-query.
- `9-cities_by_state_join.sql`: Shows cities by state using a JOIN operation.
- `10-genre_id_by_show.sql`: Lists all shows with their respective genre IDs.
- `11-genre_id_all_shows.sql`: Similar to the previous script, but includes shows without a genre.
- `12-no_genre.sql`: Lists all shows that don't have a genre.
- `13-count_shows_by_genre.sql`: Counts the number of shows by genre.
- `14-my_genres.sql`: Lists all genres of the show "Dexter".
- `15-comedy_only.sql`: Lists all shows categorized under "Comedy".
- `16-shows_by_genre.sql`: Lists all shows and their genres.

### Advanced Queries

- `100-not_my_genres.sql`: Lists genres not associated with a specific show.
- `101-not_a_comedy.sql`: Lists all shows not categorized as "Comedy".
- `102-rating_shows.sql`: Lists shows and their ratings.
- `103-rating_genres.sql`: Lists genres and their average show ratings.

### Additional Information

- `README.md`: This file provides an overview and descriptions of all scripts and files in the project.