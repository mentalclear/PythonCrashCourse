def make_album(artist_name, album_title, number_of_tracks=''):
    album_info = {"Artist": artist_name, "Album": album_title}
    if number_of_tracks:
        album_info["Number of tracks"] = number_of_tracks
        return album_info
    else:
        return album_info


print(make_album("Judas Priest", "Painkiller"))
print(make_album("Iron Maiden", "Fear Of The Dark"))
print(make_album("Iron Maiden", "Brave New World"))
print(make_album("Trivium", "Silence in the Snow", "11"))
