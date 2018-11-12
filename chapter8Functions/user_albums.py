#8.8 Python Crash Course
def make_album(artist_name, album_title, number_songs=''):
    """Returns a dictionary with artist and album name"""
    album = {'artist': artist_name, 'album': album_title}
    if number_songs:
        album['number_songs'] = number_songs
    return album

while True:
    print("\nEnter the album's information: ")
    print("(enter 'q' to quit anytime)")

    artist_name = input("Artists name: ")
    if artist_name == 'q':
        break

    album_title = input("Album title: ")
    if album_title == 'q':
        break

    album_info = make_album(artist_name, album_title)
    print(album_info)
