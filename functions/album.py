def make_album(artist_name,album_title,number_tracks = ''):
    album = {
        'artist_name' : artist_name,
        'album_title' : album_title
    }

    if number_tracks:
        album["number_tracks"] = number_tracks

    return album

album = make_album("Starset","Vessels","15")
print(album)