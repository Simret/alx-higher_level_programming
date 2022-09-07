-- List all with names in descending order of score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name <> ''
ORDER BY  score DESC;
