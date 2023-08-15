-- lists all records with a score of >= 10 in "second_table"
-- uses WHERE to specify the range of scores to pick from
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
