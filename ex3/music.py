import datetime


class Track:
    """
    Class of track.

    Args:
        title (str): name of title
        duration (datetime): duration of track
        artist (str): name of artist
        album (str): name of album
        year (int): year
    """

    def __init__(self, title, duration, artist, album, year):
        """
        The function initialises an instance of the molecule class.
        :param title (str): name of title
        :param duration (datetime): duration of track
        :param artist (str): name of artist
        :param album (str): name of album
        :param year (int): year
        """
        self.title = title
        self.duration = duration
        self.artist = artist
        self.album = album
        self.year = year

    def play(self):
        """
        Function for playing track.
        """
        print(f'Сейчас играет: {self.title}. Исполнитель: {self.artist}')

    def pause(self):
        """
        Function for pause track.
        """
        print(f'Пауза: {self.title}')

    def stop(self):
        """
        Function for stop track.
        """
        print(f'Стоп: {self.title}')


class Album:
    """
    Class of album.

    Args:
        title (str): title of album
        artist (str): name of artist
        year (int): year
        track (list): list of track in album
    """

    def __init__(self, title, artist, year):
        """
        The function initialises an instance of the molecule class.
        :param title (str): title of album
        :param artist (str): name of artist
        :param year (int): year
        """
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []

    def add_track(self, track):
        """
        Function for add track in album.
        :param track (Track): track
        :return:
        """
        self.tracks.append(track)

    def play(self):
        """
        Function for playing album.
        """
        for track in self.tracks:
            track.play()

    def pause(self):
        """
        Function for pause track in album.
        """
        for track in self.tracks:
            track.pause()

    def stop(self):
        """
        Function for pause track in album.
        """
        for track in self.tracks:
            track.stop()

    def get_total_duration(self):
        """
        Function for get total duration
        :return:
        """
        total_duration = datetime.timedelta()
        for track in self.tracks:
            total_duration += track.duration
        return total_duration
