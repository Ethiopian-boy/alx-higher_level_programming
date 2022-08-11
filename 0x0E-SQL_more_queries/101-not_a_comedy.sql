-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT tvs.title
FROM tv_shows tvs
WHERE tvs.title NOT IN (
	SELECT tvs.title
	FROM tv_shows tvs
	INNER JOIN tv_show_genres it
	ON tvs.id = it.show_id
	INNER JOIN tv_genres tvg
	ON tvg.id = it.genre_id
	WHERE name = 'Comedy')
ORDER BY tvs.title ASC;
