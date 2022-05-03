import glob
import time


start_time = time.time()

def write_directory_to_file():
    sourcefile = open('E:\Documents\Russel Record Pool\py_test.txt.txt', 'w', encoding="utf-8")
    files = glob.glob('Z:' + '/**/*.mp3', recursive=True)
    for file in files:
        sourcefile.write(file + '\n')
    sourcefile.close()
write_directory_to_file()


















print("my program took", time.time() - start_time, "seconds to run")