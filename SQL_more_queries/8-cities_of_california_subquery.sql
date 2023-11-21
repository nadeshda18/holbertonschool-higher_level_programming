-- lists all cities of california that can be found in database hbtn_0d_usa
-- states table contains record where name=california
-- results must be sorted in ascending order by cities.id
USE hbtn-0d_usa;

SET @california_id = (SELECT id FROM states WHERE name = 'California');

SELECT id, name FROM cities WHERE states_id = @california_id ORDER BY id ASC;
