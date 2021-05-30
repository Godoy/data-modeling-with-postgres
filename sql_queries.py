# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE songplays (timestamp TIMESTAMP, user_id INT, level TEXT, song_id TEXT, artist_id TEXT, session_id INT, location TEXT, user_agent TEXT)
""")

user_table_create = ("""
    CREATE TABLE users (first_name TEXT, gender CHAR, last_name TEXT, level TEXT, user_id INT)
""")

song_table_create = ("""
    CREATE TABLE songs 
        (id TEXT PRIMARY KEY, title TEXT, duration DECIMAL, year INT, artist_id TEXT NULL            
        );
""")
# CONSTRAINT fk_artist FOREIGN KEY(artist_id) REFERENCES artists(id)

artist_table_create = ("""
    CREATE TABLE artists (id TEXT PRIMARY KEY, name TEXT, latitude TEXT, longitude TEXT, location TEXT);
""")

time_table_create = ("""
    CREATE TABLE time (timestamp TIMESTAMP, hour INT, day INT, week_of_year INT, month INT, year INT, weekday INT)
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (timestamp, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users (first_name, gender, last_name, level, user_id) VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
    INSERT INTO songs (id, title, duration, year, artist_id) VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
    INSERT INTO artists (id, name, latitude, longitude, location) VALUES (%s, %s, %s, %s, %s);
""")

time_table_insert = ("""
    INSERT INTO time (timestamp, hour, day, week_of_year, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
    SELECT s.id songid, s.artist_id artistid
    FROM songs s
    LEFT JOIN artists a ON (s.artist_id = a.id)
    WHERE s.title = %s AND a.name = %s AND s.duration = %s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
