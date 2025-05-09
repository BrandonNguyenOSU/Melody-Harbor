import json
import random

def get_songs(songs,filters):
    songs_return = []
    if (filters[0]["prompt"] == "" and filters[0]["func"] == "default") or filters[0]["func"] == "include all":
        songs_return = songs
    else:
        for i in range(0,len(filters)):
            if (filters[i]["func"] == 'include' or filters[i]["func"] == 'default'):
                if (filters[i]["filter"] == 'song' or filters[i]["filter"] == 'general'):
                    for j in range(0,len(songs)):
                        if filters[i]["prompt"] == songs[j]["name"]:
                            songs_return.append(songs[j])
                if (filters[i]["filter"] == 'artist_name' or filters[i]["filter"] == 'general'):
                    for j in range(0,len(songs)):
                        if filters[i]["prompt"] == songs[j]["artist_name"]:
                            songs_return.append(songs[j])
                if (filters[i]["filter"] == 'album' or filters[i]["filter"] == 'general'):
                    for j in range(0,len(songs)):
                        if filters[i]["prompt"] == songs[j]["album"]:
                            songs_return.append(songs[j])
    for i in range(0,len(filters)):
        if (filters[i]["func"] == 'exclude'):
            if (filters[i]["filter"] == 'song' or filters[i]["filter"] == 'general'):
                j=0
                while j != len(songs_return):
                    if filters[i]["prompt"] == songs_return[j]["name"]:
                        songs_return.pop(j)
                        j-=1
                    j+=1
            if (filters[i]["filter"] == 'artist' or filters[i]["filter"] == 'general'):
                j=0
                while j != len(songs_return):
                    if filters[i]["prompt"] == songs_return[j]["artist_name"]:
                        songs_return.pop(j)
                        j-=1
                    j+=1
            if (filters[i]["filter"] == 'album' or filters[i]["filter"] == 'general'):
                j=0
                while j != len(songs_return):
                    if filters[i]["prompt"] == songs_return[j]["album"]:
                        songs_return.pop(j)
                        j-=1
                    j+=1
    return songs_return

while 1:
    # Get Songs
    call_file = open(r"call_filter.txt","r+")
    print("Listening for songs...")
    json_songs = ""
    while json_songs == "":
        json_songs = call_file.readline()
    call_file.truncate(0)
    songs = []
    if json_songs:
        songs = json.loads(json_songs)
    call_file.write("Songs received")

    # Get Filters
    print("Listening for filters...")
    json_filters = ""
    while json_filters == "":
        json_filters = call_file.readline()
    call_file.truncate(0)
    filters = []
    if json_filters:
        filters = json.loads(json_filters)

    # Run Filters and Send
    songs = get_songs(songs,filters)
    json_songs = json.dumps(songs)
    call_file.write(json_songs)
    print("Sent filtered list")
    call_file.close()