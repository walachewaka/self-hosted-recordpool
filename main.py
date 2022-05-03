from msilib.schema import Directory
from write_directory_to_variable import write_directory_to_variable, song
from analyze_mp3 import analyze_metadata, Print_Metadata
#from elasticsearch import Elasticsearch
from print_json import write_to_json, song_json
#es = Elasticsearch([{'host': '192.168.1.38', 'port': 9200}])


def main_function():
    for file in song:
        write_directory_to_variable()
        analyze_metadata()
        write_to_json()
        print(song_json)
        #Print_Metadata()
        #print(song_information)
main_function()