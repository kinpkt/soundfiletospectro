import json
import os
import shutil

# Open the JSON file
with open('emotion_label.json') as json_file:
    data = json.load(json_file)
    for file_name in data.keys():
        assigned_emo = data[file_name][0]['assigned_emo']
        
        # Move the file to the destination folder
        if os.path.isfile(file_name):
            destination_folder = os.path.join(os.getcwd(), assigned_emo)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(file_name, destination_folder)
            print(f"Moved {file_name} to {destination_folder}")
        else:
            print(f"File {file_name} does not exist.")
