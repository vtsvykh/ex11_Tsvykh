import music
import datetime

album = music.Album("Album", "Artist", 2024)

track_1 = music.Track("Track 1", datetime.timedelta(minutes=1, seconds=13), "Artist", album, 2024)
track_2 = music.Track("Track 2", datetime.timedelta(minutes=2, seconds=23), "Artist", album, 2024)
album.add_track(track_1)
album.add_track(track_2)

album.play()

album.pause()

album.stop()

total_duration = album.get_total_duration()
print(f'Общая длительность альбома: {total_duration}')
