<<<<<<< HEAD
def make_album(artist_name,album_title,number_tracks=''):
=======
def make_album(artist_name,album_title,number_tracks = ''):
>>>>>>> aabd2cbef4af96d5133557a4816f9dbc2a4d6279
    album = {
        'artist_name' : artist_name,
        'album_title' : album_title
    }

    if number_tracks:
        album["number_tracks"] = number_tracks

    return album

flag_activate = True
albums = []
while flag_activate:
    artist_name = input("Enter the name of the artist:")
    album_title = input("Enter the name of the album:")
    number_tracks = input("Enter the number of the tracks(Optional):")

    album = make_album(artist_name,album_title,number_tracks)
    albums.append(album)

    exit = input("Wanna you insert other album(Yes/No)?:")
    if exit.lower() == "no":
        flag_activate = False


print("The new albums are: ")
for album in albums:
    if album["number_tracks"]:
        print("Artist name: "+album['artist_name']+",album title: "+album['album_title']+",number tracks:"+number_tracks)
    else:
        print("Artist name: "+album['artist_name']+",album title: "+album['album_title'])
