WITH first_login AS (
  SELECT player_id, MIN(event_date) AS first_day
  FROM Activity
  GROUP BY player_id
)
SELECT
  ROUND(AVG(CASE WHEN a2.player_id IS NOT NULL THEN 1 ELSE 0 END), 2) AS fraction
FROM first_login f
LEFT JOIN Activity a2
  ON a2.player_id = f.player_id
 AND a2.event_date = DATE_ADD(f.first_day, INTERVAL 1 DAY);