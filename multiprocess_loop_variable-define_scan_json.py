from pathos.multiprocessing import ProcessingPool as Pool
from analyze_metadata import metadata_analyzer
from config import music_folder

if __name__ == '__main__':
    pool = Pool()                         # Create a multiprocessing Pool
    pool.map(metadata_analyzer, music_folder)