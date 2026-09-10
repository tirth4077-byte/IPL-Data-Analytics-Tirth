-- Query 2: Most-used venue (by matches hosted)
SELECT venue, COUNT(*) AS matches_hosted
FROM matches
GROUP BY venue
ORDER BY matches_hosted DESC
LIMIT 10;

