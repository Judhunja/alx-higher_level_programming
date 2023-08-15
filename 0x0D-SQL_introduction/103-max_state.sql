-- displays the max temp of each state
-- uses and GROUP BY state and also ORDER BY state
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
