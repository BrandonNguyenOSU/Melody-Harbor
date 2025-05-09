import json
import time

while 1:
    # Get Command
    json_list = ""
    call_file = open(r"call_storage.txt","r+")
    print("Listening for command...")
    while json_list == "":
        json_list = call_file.readline()
    call_file.truncate(0)
    print("Received command")
    if json_list and not json_list == "load":
        command = json.loads(json_list)
    else:
        command = json_list

    # Load Data
    data_file = open(r"data.txt","r+")
    json_data = data_file.readline().strip()
    data_file.seek(0)
    data_file.truncate(0)
    if json_data:
        data = json.loads(json_data)
    else:
        data = []

    # Run Command
    if command == "load":
        print("Returning data")
        json_data = json.dumps(data)
        call_file.write(json_data)
    else:
        print("Adding to storage")
        for song in command:
            data.append(song)
    
    # Store Data
    if data == []:
        json_data = ""
    else:
        json_data = json.dumps(data)
    data_file.write(json_data)

    call_file.close()
    data_file.close()