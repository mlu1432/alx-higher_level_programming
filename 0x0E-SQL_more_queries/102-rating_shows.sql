SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;