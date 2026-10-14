# =====================================================
# 작성자 : 윤완
# 작성일 : 2026-10-13
# 문제   : 07. 앨범(Album), 노래(Song), 가수(Artist), 재생목록(Playlist)
# 설계   : 1) Artist는 이름과 song_list(자기 노래 목록)를 가진다.
#          2) Song은 제목과 가수를 가진다.
#          3) Album은 이름, 가수, 발매년도, tracks(노래 목록)를 가진다.
#             add_track()은 Song을 만들어 tracks와 가수의 노래 목록에 넣는다.
#          4) Playlist는 이름과 song_list를 가지고
#             add_song()으로 노래를 추가한다.
# =====================================================


class Artist:
    def __init__(self, name):
        self.name = name
        self.song_list = []  


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Album:
    def __init__(self, name, artist, year):
        self.name = name
        self.artist = artist
        self.year = year
        self.tracks = []  

    def add_track(self, title):
        new_song = Song(title, self.artist)
        self.tracks.append(new_song)
        self.artist.song_list.append(new_song)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.song_list = []

    def add_song(self, song):
        self.song_list.append(song)


lee = Artist("Lee's Band")
album = Album("첫 번째 앨범", lee, 2020)
album.add_track("첫 번째 노래")
album.add_track("두 번째 노래")

playlist = Playlist("애창곡")

for song in album.tracks:
    playlist.add_song(song)

print("가수 :", lee.name, "/ 노래 수 :", len(lee.song_list))
print("재생목록", playlist.name, "에 담긴 노래:")
for song in playlist.song_list:
    print(" -", song.title)