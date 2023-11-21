-- lists all cities of california that can be found in database hbtn_0d_usa

-- states table contains record where name=california

-- results must be sorted in ascending order by cities.id

SELECT id, name
FROM cities
WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = 'California'
    )
ORDER BY id ASC;