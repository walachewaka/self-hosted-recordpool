import re
from turtle import title
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
import eyed3
from eyed3 import mp3
import time
from write_directory_to_variable import song

audio1 = ID3(song) #artist,album,title,bpm,initial key,date,
audio2 = MP3(song) #length
audio3 = eyed3.load(song) #publisher
audio4 = mp3.Mp3AudioFile(song) #bitrate

###########################
#global variables for JSON#
###########################
artist = ""
title = ""
album = ""
genre = ""
bpm = ""
initial_key = ""
date = ""
length = ""
publisher = ""
bitrate = ""
file_location = song
###############################
def analyze_metadata():   
    try:
        Artist = audio1['TPE1'].text[0]
#       print("Artist:",Artist) #Artist
        global artist 
        artist = Artist
    except KeyError:
        print("no artist")
    except NameError:
        print("no artist")
        pass
    try:
        Title =audio1['TIT2'].text[0]
        global title
        title = Title             
#            print("Title:",audio1['TIT2'].text[0]) #title
    except KeyError:
#        print("no title")
        pass 
    try:
        Album = audio1['TALB'].text[0]
        global album
        album = Album
#            print("Album:",audio1['TALB'].text[0]) #album
    except KeyError:
#        print("no album")
        pass
    try:
        Genre = audio3.tag.genre.name
        global genre
        genre = Genre
#            print("Genre:",audio3.tag.genre.name) #genre
    except AttributeError:
#        print("no genre")
        pass  
    try:
        Bpm = audio1['TBPM'].text[0]
        global bpm
        bpm = Bpm    
#            print("BPM:",audio1['TBPM'].text[0]) #bpm
    except KeyError:
#        print("no bpm")
        pass
    try:        
        Initial_Key = audio1['TKEY'].text[0]
        global initial_key
        initial_key = Initial_Key
#            print("Initial Key:",audio1['TKEY'].text[0]) #initial key
    except KeyError:
#        print("no key")
        pass
    try:        
        Date = audio1['TDRC'].text[0]
        global date
        date = Date
#            print("Date:",audio1['TDRC'].text[0]) #date/year
    except KeyError:
#        print("no date")
        pass

    song_length = (audio2.info.length) #length
    def convert(seconds):
        return time.strftime("%M:%S", time.gmtime(song_length))
#    print("Length",convert(song_length))
    global length
    length = time.strftime("%M:%S", time.gmtime(song_length))

    Publisher = audio3.tag.publisher
#    print("Publisher:",audio3.tag.publisher) #publisher
    global publisher
    publisher = Publisher

    song_bitrate = str(audio4.info.bit_rate)
    song_bitrate = re.sub('[^0-9]', '', song_bitrate)
#    print("Bit rate:",song_bitrate, "kbps") #bitrate
    global bitrate
    bitrate = song_bitrate
analyze_metadata()

#testing global variables for json
def Print_Metadata():
    print("Artist:",artist)
    print("Title:",title)
    print("Album:",album)
    print("Genre:",genre)
    print("BPM:",bpm)
    print("Initial Key:",initial_key)
    print("Date:",date)
    print("Length:",length)
    print("Publisher:",publisher)
    print("Bitrate:",bitrate)
    print("File Location",file_location)
#Print_Metadata()