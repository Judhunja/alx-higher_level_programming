-- lists all the comedy shows in "hbtn_0d_tvshows". Displays tv_shows.title.
-- It links tv_shows to tv_show_genres by pk/fk and tv_show_genres to tv_genres. by pk/fk
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
