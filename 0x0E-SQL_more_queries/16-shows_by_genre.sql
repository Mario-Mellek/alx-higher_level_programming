-- A script that lists all shows, and all genres linked to that show.
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, name ASC;
