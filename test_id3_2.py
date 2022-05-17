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
    AENC = ""
    APIC = ""
    ASPI = ""
    COMM = ""
    COMR = ""
    ENCR = ""
    EQU2 = ""
    ETCO = ""
    GEOB = ""
    GRID = ""
    LINK = ""
    MCDI = ""
    MLLT = ""
    OWNE = ""
    PRIV = ""
    PCNT = ""
    POPM = ""
    POSS = ""
    RBUF = ""
    RVA2 = ""
    RVRB = ""
    SEEK = ""
    SIGN = ""
    SYLT = ""
    SYTC = ""
    TALB = ""
    TBPM = ""
    TCOM = ""
    TCON = ""
    TCOP = ""
    TDEN = ""
    TDLY = ""
    TDOR = ""
    TDRC = ""
    TDRL = ""
    TDTG = ""
    TENC = ""
    TEXT = ""
    TFLT = ""
    TIPL = ""
    TIT1 = ""
    TIT2 = ""
    TIT3 = ""
    TKEY = ""
    TLAN = ""
    TLEN = ""
    TMCL = ""
    TMED = ""
    TMOO = ""
    TOAL = ""
    TOFN = ""
    TOLY = ""
    TOPE = ""
    TOWN = ""
    TPE1 = ""
    TPE2 = ""
    TPE3 = ""
    TPE4 = ""
    TPOS = ""
    TPRO = ""
    TPUB = ""
    TRCK = ""
    TRSN = ""
    TRSO = ""
    TSOA = ""
    TSOP = ""
    TSOT = ""
    TSRC = ""
    TSSE = ""
    TSST = ""
    TXXX = ""
    UFID = ""
    USER = ""
    USLT = ""
    WCOM = ""
    WCOP = ""
    WOAF = ""
    WOAR = ""
    WOAS = ""
    WORS = ""
    WPAY = ""
    WPUB = ""
    WXXX = ""

    f = open("songs_without_metadata.txt", "a")
    for file in files:
        song = file
        try:
            audio1 = ID3(song) #artist,album,title,bpm,initial key,date,
        except ID3NoHeaderError as e1:
            #print("No Metadata for", song)
            print("ERROR", e1)
            f.write(str(e1))
            f.write("\n")
            continue
        try:
            AENC = audio1['COMM'].text(0) #Comments
        except:
            pass
        try:
            APIC = audio1['COMR'].text(0) #Commercial frame
        except:
            pass
        try:
            ASPI = audio1['ENCR'].text(0) #Encryption method registration
        except:
            pass
        try:
            COMM = audio1['EQU2'].text(0) #Equalisation (2)
        except:
            pass
        try:
            COMR = audio1['ETCO'].text(0) #Event timing codes
        except:
            pass
        try:    
            ENCR = audio1['GEOB'].text(0) #General encapsulated object
        except:
            pass
        try:
            EQU2 = audio1['GRID'].text(0) #Group identification registration
        except:
            pass
        try:
            ETCO = audio1['LINK'].text(0) #Linked information
        except:
            pass
        try:
            GEOB = audio1['MCDI'].text(0) #Music CD identifier
        except:
            pass
        try:
            GRID = audio1['MLLT'].text(0) #MPEG location lookup table
        except:
            pass
        try:
            LINK = audio1['OWNE'].text(0) #Ownership frame
        except:
            pass
        try:
            MCDI = audio1['PRIV'].text(0) #Private frame
        except:
            pass
        try:            
            MLLT = audio1['PCNT'].text(0) #Play counter
        except:
            pass
        try:            
            OWNE = audio1['POPM'].text(0) #Popularimeter
        except:
            pass
        try:            
            PRIV = audio1['POSS'].text(0) #Position synchronisation frame
        except:
            pass
        try:            
            PCNT = audio1['RBUF'].text(0) #Recommended buffer size
        except:
            pass
        try:            
            POPM = audio1['RVA2'].text(0) #Relative volume adjustment (2)
        except:
            pass
        try:            
            POSS = audio1['RVRB'].text(0) #Reverb
        except:
            pass
        try:            
            RBUF = audio1['SEEK'].text(0) #Seek frame
        except:
            pass
        try:            
            RVA2 = audio1['SIGN'].text(0) #Signature frame
        except:
            pass
        try:            
            RVRB = audio1['SYLT'].text(0) #Synchronised lyric/text
        except:
            pass
        try:            
            SEEK = audio1['SYTC'].text(0) #Synchronised tempo codes
        except:
            pass
        try:            
            SIGN = audio1['TALB'].text(0) #Album/Movie/Show title
        except:
            pass
        try:            
            SYLT = audio1['TBPM'].text(0) #BPM (beats per minute)
        except:
            pass
        try:            
            SYTC = audio1['TCOM'].text(0) #Composer
        except:
            pass
        try:            
            TALB = audio1['TCON'].text(0) #Content type
        except:
            pass
        try:            
            TBPM = audio1['TCOP'].text(0) #Copyright message
        except:
            pass
        try:            
            TCOM = audio1['TDEN'].text(0) #Encoding time
        except:
            pass
        try:            
            TCON = audio1['TDLY'].text(0) #Playlist delay
        except:
            pass
        try:            
            TCOP = audio1['TDOR'].text(0) #Original release time
        except:
            pass
        try:            
            TDEN = audio1['TDRC'].text(0) #Recording time
        except:
            pass
        try:            
            TDLY = audio1['TDRL'].text(0) #Release time
        except:
            pass
        try:            
            TDOR = audio1['TDTG'].text(0) #Tagging time
        except:
            pass
        try:            
            TDRC = audio1['TENC'].text(0) #Encoded by
        except:
            pass
        try:            
            TDRL = audio1['TEXT'].text(0) #Lyricist/Text writer
        except:
            pass
        try:            
            TDTG = audio1['TFLT'].text(0) #File type
        except:
            pass
        try:            
            TENC = audio1['TIPL'].text(0) #Involved people list
        except:
            pass
        try:            
            TEXT = audio1['TIT1'].text(0) #Content group description
        except:
            pass
        try:            
            TFLT = audio1['TIT2'].text(0) #Title/songname/content description
        except:
            pass
        try:            
            TIPL = audio1['TIT3'].text(0) #Subtitle/Description refinement
        except:
            pass
        try:            
            TIT1 = audio1['TKEY'].text(0) #Initial key
        except:
            pass
        try:            
            TIT2 = audio1['TLAN'].text(0) #Language(s)
        except:
            pass
        try:            
            TIT3 = audio1['TLEN'].text(0) #Length
        except:
            pass
        try:            
            TKEY = audio1['TMCL'].text(0) #Musician credits list
        except:
            pass
        try:            
            TLAN = audio1['TMED'].text(0) #Media type
        except:
            pass
        try:            
            TLEN = audio1['TMOO'].text(0) #Mood
        except:
            pass
        try:            
            TMCL = audio1['TOAL'].text(0) #Original album/movie/show title
        except:
            pass
        try:            
            TMED = audio1['TOFN'].text(0) #Original filename
        except:
            pass
        try:            
            TMOO = audio1['TOLY'].text(0) #Original lyricist(s)/text writer(s)
        except:
            pass
        try:            
            TOAL = audio1['TOPE'].text(0) #Original artist(s)/performer(s)
        except:
            pass
        try:            
            TOFN = audio1['TOWN'].text(0) #File owner/licensee
        except:
            pass
        try:            
            TOLY = audio1['TPE1'].text(0) #Lead performer(s)/Soloist(s)
        except:
            pass
        try:            
            TOPE = audio1['TPE2'].text(0) #Band/orchestra/accompaniment
        except:
            pass
        try:            
            TOWN = audio1['TPE3'].text(0) #Conductor/performer refinement
        except:
            pass
        try:            
            TPE1 = audio1['TPE4'].text(0) #Interpreted, remixed, or otherwise modified by
        except:
            pass
        try:            
            TPE2 = audio1['TPOS'].text(0) #Part of a set
        except:
            pass
        try:            
            TPE3 = audio1['TPRO'].text(0) #Produced notice
        except:
            pass
        try:            
            TPE4 = audio1['TPUB'].text(0) #Publisher
        except:
            pass
        try:            
            TPOS = audio1['TRCK'].text(0) #Track number/Position in set
        except:
            pass
        try:            
            TPRO = audio1['TRSN'].text(0) #Internet radio station name
        except:
            pass
        try:            
            TPUB = audio1['TRSO'].text(0) #Internet radio station owner
        except:
            pass
        try:            
            TRCK = audio1['TSOA'].text(0) #Album sort order
        except:
            pass
        try:            
            TRSN = audio1['TSOP'].text(0) #Performer sort order
        except:
            pass
        try:            
            TRSO = audio1['TSOT'].text(0) #Title sort order
        except:
            pass
        try:            
            TSOA = audio1['TSRC'].text(0) #ISRC (international standard recording code)
        except:
            pass
        try:            
            TSOP = audio1['TSSE'].text(0) #Software/Hardware and settings used for encoding
        except:
            pass
        try:            
            TSOT = audio1['TSST'].text(0) #Set subtitle
        except:
            pass
        try:            
            TSRC = audio1['TXXX'].text(0) #User defined text information frame
        except:
            pass
        try:            
            TSSE = audio1['UFID'].text(0) #Unique file identifier
        except:
            pass
        try:            
            TSST = audio1['USER'].text(0) #Terms of use
        except:
            pass       
        print(TIT1)
metadata_analyzer()