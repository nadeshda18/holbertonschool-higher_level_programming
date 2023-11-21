-- lists all cities of california that can be found in database hbtn_0d_usa
-- states table contains record where name=california
-- results must be sorted in ascending order by cities.id
USE hbtn-0d_usa;

SELECT cities.id, cities.name FROM cities, states WHERE cities.states_id = states.id AND states.name = 'California' ORDER BY cities.id ASC;
