class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = artist_count

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1


if __name__ == "__main__":
    songs = [
        Song("99 Problems", "Jay Z", "Rap"),
        Song("Halo", "Beyonce", "Pop"),
        Song("Smells Like Teen Spirit", "Nirvana", "Rock"),
    ]

    print("Songs:")
    for song in songs:
        print(f"- {song.name} by {song.artist} ({song.genre})")
    print(f"Total songs: {Song.count}")
    print(f"Artists: {Song.artists}")
    print(f"Genres: {Song.genres}")
    print(f"Songs by artist: {Song.artist_count}")
    print(f"Songs by genre: {Song.genre_count}")
