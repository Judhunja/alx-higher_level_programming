-- lists all cities contained in "hbtn_0d_usa"
-- displays cities.id - cities.name - state.name
SELECT cities.id, cities.name, states.name
FROM cities JOIN states
WHERE city.states_id = states.id
ORDER BY cities.id ASC;
