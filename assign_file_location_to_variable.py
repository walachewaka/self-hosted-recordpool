def assign_fiie_location_to_variable():
    filepath = 'E:\Documents\Russel Record Pool\py_test.txt.txt'
    with open(filepath, 'r') as fp:
        for line in fp:
            global song_location
            song_location = line
            #print(song_location)
assign_fiie_location_to_variable()
#print(song_location)
