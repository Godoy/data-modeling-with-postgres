# About 
The database resulting from this ETL is an aggregation of information about songs and artists and the logs of users' activities over time. 
With this information arranged in an optimized way for analytical view, the Sparkify team will be able to better understand the behavior of its users, their profiles and the most listened to music in the most varied dimensions.

# About the design
The ETL was built in python using pandas library to optimize data transformation and aggregation from the two data sources (songs and logs). The database was built based on a star schema, using the song plays as a fact table. To allow filters and groupings, these dimension tables were created: users, songs, artists and time.

# Getting Started
1. To create the database structure, runs `python create_tables.py`
2. To run the ETL: `python  etl.py`
3. After that, the database will be already created and populated with all information.

## Query examples 
1. Get the most listened to songs from free users: