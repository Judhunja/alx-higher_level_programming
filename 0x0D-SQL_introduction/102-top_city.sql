-- displays top 3 city temps during July and August, ordered by temp(DESC)
-- groups by city
SELECT DISTINCT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
