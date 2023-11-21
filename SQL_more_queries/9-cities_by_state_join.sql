-- lists all cities contained database hbtn_0d_usa
-- display: cities.id - cities.name - states.name
-- results must be sorted in ascending order by cities.id
-- You can only use one SELECT statement
USE hbtn_0d_usa
SELECT cities.id, cities.name, states.name AS state_name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
