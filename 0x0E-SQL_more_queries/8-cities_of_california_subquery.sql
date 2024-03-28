-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- lists all rows of a column in a database
-- lists all cities contained in the database hbtn_0d_usa
-- lists all rows of a particular column in a database

SELECT cities.name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California';