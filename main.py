from msilib.schema import Directory
from write_directory_to_variable import write_directory_to_variable, song
from analyze_mp3 import analyze_metadata, Print_Metadata
#from elasticsearch import Elasticsearch
from print_json import write_to_json, json_song_info
#es = Elasticsearch([{'host': '192.168.1.38', 'port': 9200}])


def main_function():
    for song_information in song:
        write_directory_to_variable()
        analyze_metadata()
        write_to_json()
        print(json_song_info)
        #Print_Metadata()
        #print(song_information)
main_function()






#es.indices.refresh(index="test-index")


