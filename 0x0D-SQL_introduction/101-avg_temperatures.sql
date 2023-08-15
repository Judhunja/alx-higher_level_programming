-- displays average temp by city ordered by temperature in DESC
-- uses temperatures.sql file
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
