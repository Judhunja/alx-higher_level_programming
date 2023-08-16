-- lists all cities of California in the database "hbtn_0d_usa"
-- selects only the cities where the state is California
USE hbtn_0d_usa;
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
GROUP BY id
ORDER BY id ASC;
