import json

def alpha_sort(songs,var,is_reverse):
    new_songs = sorted(songs, key=lambda d: d[var])
    if is_reverse:
        new_songs.reverse()
    return new_songs
                
                
def handle_method(method):
    print(method)
    if method["order"] == "abc":
        return alpha_sort(method["songs"],method["sortby"],False)
    elif method["order"] == "cba":
        return alpha_sort(method["songs"],method["sortby"],True)

while 1:
    # Get Command
    json_list = ""
    call_file = open(r"call_sorting.txt","r+")
    print("Listening for list to sort...")
    while json_list == "":
        json_list = call_file.readline()
    call_file.truncate(0)
    songs = []
    if json_list:
        method = json.loads(json_list)
    songs = handle_method(method)
    json_songs = json.dumps(songs)
    call_file.write(json_songs)
    print("Sent sorted list")
    call_file.close()