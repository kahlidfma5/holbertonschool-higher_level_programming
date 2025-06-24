-- Script that displays the max temperature of each state
-- Query to display the max temperature of each state
SELECT s.name
FROM states s
JOIN cities c ON c.state_id = s.id
GROUP BY s.id
ORDER BY COUNT(c.id) DESC
LIMIT 1;
