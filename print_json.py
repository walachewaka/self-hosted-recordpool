import json
from analyze_mp3 import artist, title, album, genre, bpm, initial_key, date, length, publisher, bitrate, file_location

def write_to_json():
    global json_song_info
    json_song_info = {
            "artist": artist,
            "title": title,
            "album": album,
            "genre": genre,
            "bpm": bpm,
            "initial_key": initial_key,
            "date": date,
            "length": length,
            "publisher": publisher,
            "bitrate": bitrate,
            "song location": file_location
        }
write_to_json()

song_json = json.dumps(str(json_song_info))
print(json_song_info)