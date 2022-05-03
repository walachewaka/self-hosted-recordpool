from calendar import prmonth
import glob
import time

start_time = time.time()

def write_directory_to_variable():
    files = glob.glob('Z:' + '/**/*.mp3', recursive=True)
    for file in files:
        global song
        song = file
        #print(song)
write_directory_to_variable()

#print("my program took", time.time() - start_time, "seconds to run")