# About
The database resulting from this ETL is an aggregation of information about songs and artists and the logs of users' activities over time.
With this information arranged in an optimized way for analytical view, the Sparkify team will be able to better understand the behavior of its users, their profiles and the most listened to music in the most varied dimensions.

# Solution Design
The ETL was built in python using pandas library to optimize data transformation and aggregation from the two data sources (songs and logs). The database was built based on a star schema, using the song plays as a fact table. To allow filters and groupings, these dimension tables were created: users, songs, artists and time.

# Getting Started
1. To create the database structure, runs `python create_tables.py`
2. To run the ETL: `python  etl.py`
3. After that, the database will be already created and populated with all available information.

## Query examples
1. Get the top 10 listened songs from "free" level:
```
    SELECT s.title song, COUNT(*) total
    FROM songplays sp
    INNER JOIN songs s ON (s.song_id = sp.song_id)
    WHERE level = 'free' GROUP BY s.title ORDER BY song DESC  LIMIT 10
```

2. Get the top 10 listened songs from artists with location "California - LA":
```
    SELECT a.name artist, COUNT(*) total
    FROM songplays sp
    INNER JOIN artists a ON (a.artist_id = sp.artist_id)
    WHERE a.location = 'California - LA'
    GROUP BY a.name ORDER BY total DESC  LIMIT 10
```

3. User genders distribution of users that heard music artists with location "California - LA":
```
    SELECT u.gender, COUNT(u.gender) total
    FROM songplays sp
    INNER JOIN artists a ON (a.artist_id = sp.artist_id)
    INNER JOIN users u ON (u.user_id = sp.user_id)
    WHERE a.location = 'California - LA' GROUP BY u.gender ORDER BY total DESC
```