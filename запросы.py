import sqlalchemy
import psycopg2
engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/py48')

connection = engine.connect()

# # print(connection.execute("""SELECT * FROM collection;""").fetchall())
connection.execute("""UPDATE albums
    SET album_year = 2018
    WHERE id = 17;
""")

# название и год выхода альбомов, вышедших в 2018 году;
print(connection.execute("""SELECT album_name, album_year FROM albums
    WHERE album_year = 2018;
""").fetchall())

# название и продолжительность самого длительного трека
print(connection.execute("""SELECT song_name, song_time FROM songs
    ORDER BY song_time DESC
    LIMIT 1;
""").fetchall())

# название треков, продолжительность которых не менее 3,5 минуты;
print(connection.execute("""SELECT song_name FROM songs
    WHERE song_time >= 3.5
""").fetchall())

# названия сборников, вышедших в период с 2018 по 2020 год включительно
print(connection.execute("""SELECT collection_name FROM collection
    WHERE collectin_year BETWEEN 2018 AND 2020;
""").fetchall())

# исполнители, чье имя состоит из 1 слова
print(connection.execute("""SELECT singer_nickname FROM singers
    WHERE singer_nickname NOT LIKE '%% %%';
""").fetchall())

# название треков, которые содержат слово "мой"/"my"
print(connection.execute("""SELECT song_name FROM songs
    WHERE song_name ILIKE '%%my%%';
""").fetchall())