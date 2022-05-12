import glob
import time
from config import music_folder
import re
from mutagen.id3 import ID3, ID3Warning, ID3NoHeaderError
from mutagen.mp3 import MP3, HeaderNotFoundError
import eyed3
from eyed3 import mp3
import json
import os

def metadata_analyzer():
    start_time = time.time()
    files = glob.iglob(music_folder + '/**/*.mp3', recursive=True)
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
    exceptions = (AttributeError, HeaderNotFoundError, ID3NoHeaderError)
    #exception_count = sum(1 for e in exceptions if e)
    for file in files:
        song = file
        try:
            audio1 = ID3(song) #artist,album,title,bpm,initial key,date,
        except ID3NoHeaderError as e1:
            #print("No Metadata for", song)
            #print("Audio 1", e1)
            pass
        try:
            audio2 = MP3(song) #length
        except HeaderNotFoundError as e2:
            #print("Audio 2", e2)
            pass
        audio3 = eyed3.load(song) #publisher,genre
        try:
            audio4 = mp3.Mp3AudioFile(song) #bitrate
        except AttributeError as e3:
            #print("Audio 3",e3)
            pass
        ##need to break loop if 2 errors above here
        try:
            Artist = audio1['TPE1'].text[0]
            #print("Artist:",Artist) #Artist
            artist = Artist
        except (KeyError, NameError, AttributeError):
            #print("no artist")
            pass
        try:
            Title = audio1['TIT2'].text[0]
            title = Title             
        #    #print("Title:",audio1['TIT2'].text[0]) #title
        except (KeyError, AttributeError):
            #print("no title")
            pass 
        try:
            Album = audio1['TALB'].text[0]
            album = Album
            #print("Album:",audio1['TALB'].text[0]) #album
        except (KeyError, NameError, AttributeError):
            #print("no album")
            pass
        try:
            Genre = audio3.tag.genre.name
            genre = Genre
            #print("Genre:",audio3.tag.genre.name) #genre
        except (AttributeError, ID3Warning):
            #print("no genre")
            pass
        try:
            Bpm = audio1['TBPM'].text[0]
            bpm = Bpm
        #    #print("BPM:",audio1['TBPM'].text[0]) #bpm
        except (KeyError, AttributeError):
            #print("no bpm")
            pass
        try:        
            Initial_Key = audio1['TKEY'].text[0]
            initial_key = Initial_Key
            #print("Initial Key:",audio1['TKEY'].text[0]) #initial key
        except KeyError:
            #print("no key")
            pass
        try:        
            Date = audio1['TDRC'].text[0]
            date = Date
            #print("Date:",audio1['TDRC'].text[0]) #date/year
        except KeyError:
            #print("no date")
            pass
        try:
            song_length = (audio2.info.length) #length
            def convert(seconds):
                return time.strftime("%M:%S", time.gmtime(song_length))
            #print("Length:",convert(song_length))
            length = time.strftime("%M:%S", time.gmtime(song_length))
        except(HeaderNotFoundError) as error:
        #   print(error, song)
           pass
        try:
            Publisher = audio3.tag.publisher
            #print("Publisher:",audio3.tag.publisher) #publisher
            publisher = Publisher
        except (AttributeError):
            #print("No Publisher")
            pass
        try:
            song_bitrate = str(audio4.info.bit_rate)
            song_bitrate = re.sub('[^0-9]', '', song_bitrate)
            #print("Bit rate:",song_bitrate, "kbps") #bitrate
            bitrate = song_bitrate
            #print("File Location:",file_location, '\n')
        except AttributeError:
            pass
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
        "song location": song
        }
        song_json = json.dumps(str(json_song_info))
        print(song_json, '\n')
    end_time = time.time()
    Program_Duration = end_time - start_time
    program_duration = time.strftime("%H:%M:%S", time.gmtime(Program_Duration))
    file_count = sum(len(files) for _, _, files in os.walk(music_folder))
    print("The program took", program_duration, "to scan", file_count, "songs")
metadata_analyzer()