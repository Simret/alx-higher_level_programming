-- Filte table by city in ascending order
SELECT id, name FROM cities c
WHERE c.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
