def make_album(artist_name, album_title, number_of_tracks=''):
    album_info = {"Artist": artist_name, "Album": album_title}
    if number_of_tracks:
        album_info["Number of tracks"] = number_of_tracks
        return album_info
    else:
        return album_info


while True:
    print("\nPlease input album information")
    print("(press 'q' any time to quit)")
    art_name = input("Artist name: ")
    if art_name == 'q':
        break
    alb_title = input("Album title: ")
    if alb_title == 'q':
        break

    print("\nThe album submitted:")
    print(make_album(art_name, alb_title))
