-- Lists all cities with their respective states from hbtn_0d_usa database, sorted by cities.id.
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
