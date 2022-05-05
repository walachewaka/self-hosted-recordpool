import glob
import time
from config import music_folder
import re
from mutagen.id3 import ID3, ID3NoHeaderError, ID3Warning
from mutagen.mp3 import MP3, HeaderNotFoundError, MutagenError, InvalidMPEGHeader
import eyed3
import mutagen
from mutagen import MutagenError
from eyed3 import mp3
import json

start_time = time.time()

def write_directory_to_variable():
    files = glob.iglob(music_folder + '/**/*.mp3', recursive=True)
    for file in files:
        song = file
        audio1 = ID3(song) #artist,album,title,bpm,initial key,date,
        audio2 = MP3(song) #length
        audio3 = eyed3.load(song) #publisher,genre
        audio4 = mp3.Mp3AudioFile(song) #bitrate
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

        try:
            Artist = audio1['TPE1'].text[0]
            #print("Artist:",Artist) #Artist
            #global artist 
            artist = Artist
        except (KeyError, MutagenError, HeaderNotFoundError, ID3NoHeaderError, NameError, ID3Warning, mutagen.MutagenError, ID3NoHeaderError):
            #print("no artist")
            pass
        try:
            Title = audio1['TIT2'].text[0]
            #global title
            title = Title             
            #print("Title:",audio1['TIT2'].text[0]) #title
        except KeyError:
            #print("no title")
            pass 
        try:
            Album = audio1['TALB'].text[0]
            album = Album
            #print("Album:",audio1['TALB'].text[0]) #album
        except (KeyError, NameError):
            #print("no album")
            pass
        try:
            Genre = audio3.tag.genre.name
            #global genre
            genre = Genre
            #print("Genre:",audio3.tag.genre.name) #genre
        except (AttributeError, ID3Warning):
            #print("no genre")
            pass
        try:
            Bpm = audio1['TBPM'].text[0]
            bpm = Bpm
            #print("BPM:",audio1['TBPM'].text[0]) #bpm
        except KeyError:
            #print("no bpm")
            pass
        try:        
            Initial_Key = audio1['TKEY'].text[0]
            #global initial_key
            initial_key = Initial_Key
            #print("Initial Key:",audio1['TKEY'].text[0]) #initial key
        except KeyError:
            #print("no key")
            pass
        try:        
            Date = audio1['TDRC'].text[0]
            #global date
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
            #global length
            length = time.strftime("%M:%S", time.gmtime(song_length))
        except (MutagenError, HeaderNotFoundError, InvalidMPEGHeader) as error:
            #print(error, song)
            pass

        Publisher = audio3.tag.publisher
        #print("Publisher:",audio3.tag.publisher) #publisher
        #global publisher
        publisher = Publisher

        song_bitrate = str(audio4.info.bit_rate)
        song_bitrate = re.sub('[^0-9]', '', song_bitrate)
        #print("Bit rate:",song_bitrate, "kbps") #bitrate
        #global bitrate
        bitrate = song_bitrate
        #print("File Location:",file_location, '\n')
       
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
        song_json = json.dumps(str(json_song_info))
        print(song_json, '\n')
write_directory_to_variable()

print("my program took", time.time() - start_time, "seconds to run")