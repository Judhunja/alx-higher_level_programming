-- lists all shows without the genre comedy
-- results are ordered by show title
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres 0N tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
)
ORDER BY tv_shows.title ASC;
