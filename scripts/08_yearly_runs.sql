-- Query 6: Season-wise total runs scored (trend over time)
SELECT m.season, SUM(d.total_runs) AS total_runs
FROM deliveries d
JOIN matches m ON d.match_id = m.id
GROUP BY m.season
ORDER BY m.season;