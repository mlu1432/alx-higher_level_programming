SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_genres.name != 'Comedy' OR tv_genres.name IS NULL
ORDER BY tv_shows.title ASC;