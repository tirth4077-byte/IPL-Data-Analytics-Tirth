-- Query 5: Most frequent Player of the Match winners
SELECT player_of_match, COUNT(*) AS awards
FROM matches
WHERE player_of_match != 'Not Awarded'
GROUP BY player_of_match
ORDER BY awards DESC
LIMIT 10;

