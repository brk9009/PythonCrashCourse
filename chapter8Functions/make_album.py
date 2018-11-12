#8.7 Python Crash Course
def make_album(artist_name, album_title, number_songs=''):
    """Returns a dictionary with artist and album name"""
    album = {'artist': artist_name, 'album': album_title}
    if number_songs:
        album['number_songs'] = number_songs
    return album

eminem = make_album('Eminem', 'Rap God')
print(eminem)

dolla = make_album('Ty Dolla $ign', 'Saved')
print(dolla)

space_jam = make_album('Elvis Costello', 'This Years Model', 5)
print(space_jam)
