SELECT tv_genres.name, SUM(tv_shows.rating) AS rating_sum
FROM tv_genres
JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
JOIN tv_shows ON tv_shows_genres.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;