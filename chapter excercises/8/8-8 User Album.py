def make_album(artist_name, album_title, tracks=None):
    details = {
        'Artist': artist_name.title(),
        'Album Name': album_title.title()
        # 'Numbers of tracks': tracks.title()
    }
    if tracks:
        details['tracks'] = tracks
    return details


album = make_album('Linkin Park', 'Meteora', tracks=25)
print(album)

album = make_album('Ishiyama', 'AOT', tracks=50)
print(album)

album = make_album('Doja Cat', 'Minx', tracks=20)
print(album)

while True:
    print("Please tell me the artist name:")
    print("(enter 'q' at any time to exit)")

    singer_name = input("Artist Name: ")
    if singer_name == 'q':
        break

    album_name = input("Album Name:")
    if album_name == 'q':
        break

    formatted_singer_and_album_name = make_album(singer_name, album_name)
    print(f"\nHello, {formatted_singer_and_album_name} :)")
