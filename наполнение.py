import sqlalchemy
import psycopg2
engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/py48')

connection = engine.connect()
connection.execute("""INSERT INTO singers(singer_nickname)
    VALUES('JEON SOMI');
""")
сonnection.execute("""INSERT INTO singers(singer_nickname)
   VALUES('James Blunt');
""")
connection.execute("""INSERT INTO singers(singer_nickname)
   VALUES('Helloween');
""")
connection.execute("""INSERT INTO singers(singer_nickname)
   VALUES('The Driver era');
""")
connection.execute("""INSERT INTO singers(singer_nickname)
   VALUES('Aria');
""")
connection.execute("""INSERT INTO singers(singer_nickname)
   VALUES('Вокруг фонарного столба');
""")
connection.execute("""INSERT INTO singers(singer_nickname)
   VALUES('Группа Секрет');
""")
connection.execute("""INSERT INTO singers(singer_nickname)
   VALUES('Selena Gomez');
""")
print(connection.execute("""SELECT * FROM singers;""").fetchall())


connection.execute("""INSERT INTO albums(album_name, album_year)
    VALUES('XOXO', 2021);
""")
connection.execute("""INSERT INTO albums(album_name, album_year)
    VALUES('The Stars', 2018);
""")
connection.execute("""INSERT INTO albums(album_name, album_year)
    VALUES('Metal Jukebox', 1994);
""")
connection.execute("""INSERT INTO albums(album_name, album_year)
    VALUES('X', 2020);
""")
connection.execute("""INSERT INTO albums(album_name, album_year)
    VALUES('Легенды', 1998);
""")
connection.execute("""INSERT INTO albums(album_name, album_year)
    VALUES('Кино', 2020);
""")
connection.execute("""INSERT INTO albums(album_name, album_year)
    VALUES('Секрет', 1987);
""")
connection.execute("""INSERT INTO albums(album_name, album_year)
    VALUES('Rare', 2021);
""")

print(connection.execute("""SELECT * FROM albums;""").fetchall())

connection.execute("""INSERT INTO genres(genres_name)
    VALUES('K-Pop');
""")
connection.execute("""INSERT INTO genres(genres_name)
    VALUES('Pop');
""")
connection.execute("""INSERT INTO genres(genres_name)
    VALUES('Metal');
""")
connection.execute("""INSERT INTO genres(genres_name)
    VALUES('Alternative');
""")
connection.execute("""INSERT INTO genres(genres_name)
    VALUES('Rock');
""")
connection.execute("""INSERT INTO genres(genres_name)
    VALUES('Indie Rock');
""")

print(connection.execute("""SELECT * FROM genres;""").fetchall())


connection.execute("""INSERT INTO genressing(id_singer, id_genres)
    VALUES('1','1');
""")
connection.execute("""INSERT INTO genressing(id_singer, id_genres)
    VALUES('2','2');
""")
connection.execute("""INSERT INTO genressing(id_singer, id_genres)
    VALUES('3','3');
""")
connection.execute("""INSERT INTO genressing(id_singer, id_genres)
    VALUES('4','4');
""")
connection.execute("""INSERT INTO genressing(id_singer, id_genres)
    VALUES('5','5');
""")
connection.execute("""INSERT INTO genressing(id_singer, id_genres)
    VALUES('6','6');
""")
connection.execute("""INSERT INTO genressing(id_singer, id_genres)
    VALUES('7','5');
""")
connection.execute("""INSERT INTO genressing(id_singer, id_genres)
    VALUES('8','2');
""")

print(connection.execute("""SELECT * FROM genressing;""").fetchall())



connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('My Birthday','3.06', '16');
""")
connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Anymore','3.18', '16');
""")
connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Watermelon','3.08', '16');
""")

connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('My monsters','4.20', '17');
""")
connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('The truth','3.43', '17');
""")
connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Champions','3.13', '17');
""")

connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Hocus Pocus','6.44', '18');
""")
connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Mexican','4.48', '18');
""")

connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Low','3.30', '19');
""")
connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Natural','3.16', '19');
""")

connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Беспечный ангел','3.58', '20');
""")

connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Клише','2.47', '21');
""")
connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Кино','2.52', '21');
""")
connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Хочешь','4.27', '21');
""")

connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Буги-вуги','3.22', '22');
""")

connection.execute("""INSERT INTO songs(song_name, song_time, album_id)
    VALUES('Rare','3.48', '23');
""")

print(connection.execute("""SELECT * FROM songs;""").fetchall())


connection.execute("""INSERT INTO albumsing(id_singer, id_albums)
    VALUES('1', '16');
""")
connection.execute("""INSERT INTO albumsing(id_singer, id_albums)
    VALUES('2', '17');
""")
connection.execute("""INSERT INTO albumsing(id_singer, id_albums)
    VALUES('3', '18');
""")
connection.execute("""INSERT INTO albumsing(id_singer, id_albums)
    VALUES('4', '19');
""")
connection.execute("""INSERT INTO albumsing(id_singer, id_albums)
    VALUES('5', '20');
""")
connection.execute("""INSERT INTO albumsing(id_singer, id_albums)
    VALUES('6', '21');
""")
connection.execute("""INSERT INTO albumsing(id_singer, id_albums)
    VALUES('7', '22');
""")
connection.execute("""INSERT INTO albumsing(id_singer, id_albums)
    VALUES('8', '23');
""")
print(connection.execute("""SELECT * FROM albumsing;""").fetchall())

connection.execute("""INSERT INTO collection(collection_name, collectin_year)
    VALUES('Топ-100 корейских песен за март', 2021);
""")
connection.execute("""INSERT INTO collection(collection_name, collectin_year)
    VALUES('Sad time', 2020);
""")
connection.execute("""INSERT INTO collection(collection_name, collectin_year)
    VALUES('Metal time', 2018);
""")
connection.execute("""INSERT INTO collection(collection_name, collectin_year)
    VALUES('American boy', 2021);
""")
connection.execute("""INSERT INTO collection(collection_name, collectin_year)
    VALUES('Классика', 2020);
""")
connection.execute("""INSERT INTO collection(collection_name, collectin_year)
    VALUES('Новые люди', 2021);
""")
connection.execute("""INSERT INTO collection(collection_name, collectin_year)
    VALUES('Стиляги', 2015);
""")
connection.execute("""INSERT INTO collection(collection_name, collectin_year)
    VALUES('Rare', 2021);
""")

print(connection.execute("""SELECT * FROM collection;""").fetchall())

connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('4', '1');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('5', '1');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('6', '1');
""")

connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('7', '2');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('8', '2');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('9', '2');
""")

connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('10', '3');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('11', '3');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('12', '4');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('13', '4');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('14', '5');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('15', '6');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('16', '6');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('17', '6');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('18', '7');
""")
connection.execute("""INSERT INTO collectionsongs(id_song, id_collection)
    VALUES('19', '8');
""")


print(connection.execute("""SELECT * FROM collectionsongs;""").fetchall())

