-- lists all records in "second_table" that have a 'name' value
-- should display score, name. Records should be in DESC
SELECT score, name
FROM second_table
WHERE name <> 'NULL'
ORDER BY score DESC, name DESC;
