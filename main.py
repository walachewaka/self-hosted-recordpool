from analyze_mp3 import analyze_metadata
from assign_file_location_to_variable import assign_fiie_location_to_variable
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '192.168.1.38', 'port': 9200}])

es.indices.refresh(index="test-index")