from mutagen.id3 import ID3, COMM, ID3NoHeaderError, ID3Warning
song = "Z:/Coolio x Fuzz vs Acraze & Cherish vs. Interupt - Do It Gangstas Paradise (Pat C's 'Show Me' Bootleg) (Intro Clean) 5A 130.mp3"

try:
    song_tags = ID3(song)
    print(song_tags.pprint)
except (ID3NoHeaderError):
    ID3(song).add(COMM(encoding=3, text="comment"))
    ID3(song).save
    print("ERROR")
    #song_tags.add(COMM(encoding=3, text="this is a comm"))
    #song_tags.save()