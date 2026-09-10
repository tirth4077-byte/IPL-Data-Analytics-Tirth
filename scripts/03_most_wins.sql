-- ============================================
-- Stage 3: SQL Data Analysis
-- IPL Data Analytics Project
-- ============================================

-- Query 1: Team with most wins overall
SELECT winner, COUNT(*) AS total_wins
FROM matches
WHERE winner != 'No Result'
GROUP BY winner
ORDER BY total_wins DESC
LIMIT 10;

