(
SELECT u.name as results
FROM Users u
JOIN MovieRating mr
    ON mr.user_id = u.user_id
GROUP BY mr.user_id
ORDER BY COUNT(*) DESC, u.name ASC
LIMIT 1
)

UNION ALL

(
SELECT m.title as results
FROM Movies m
JOIN MovieRating mr
    ON mr.movie_id = m.movie_id
WHERE mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01'
GROUP BY mr.movie_id
ORDER BY AVG(mr.rating) DESC, m.title ASC
LIMIT 1
)