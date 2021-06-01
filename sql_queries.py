# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE songplays (songplay_id SERIAL PRIMARY KEY, start_time TIMESTAMP NOT NULL, user_id INT NOT NULL, level TEXT, song_id TEXT, artist_id TEXT, session_id INT, location TEXT, user_agent TEXT)
""")

user_table_create = ("""
    CREATE TABLE users (user_id INT PRIMARY KEY, first_name TEXT, gender CHAR, last_name TEXT, level TEXT)
""")

song_table_create = ("""
    CREATE TABLE songs (song_id TEXT PRIMARY KEY, title TEXT, duration DECIMAL, year INT, artist_id TEXT NOT NULL);
""")

artist_table_create = ("""
    CREATE TABLE artists (artist_id TEXT PRIMARY KEY, name TEXT, latitude FLOAT, longitude FLOAT, location TEXT);
""")

time_table_create = ("""
    CREATE TABLE time (start_time TIMESTAMP PRIMARY KEY, hour INT, day INT, week INT, month INT, year INT, weekday INT)
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, gender, last_name, level) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, duration, year, artist_id) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, latitude, longitude, location) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id songid, s.artist_id artistid
    FROM songs s
    LEFT JOIN artists a ON (s.artist_id = a.artist_id)
    WHERE s.title = %s AND a.name = %s AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
