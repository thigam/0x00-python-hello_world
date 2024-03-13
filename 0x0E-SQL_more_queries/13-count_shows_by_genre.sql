-- Lisst all gernes from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genres.genre_id IS NOT NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
SELECT tv_genres.name, COUNT(tv_shows.id) FROM tv_genres RIGHT JOIN tv_shows
