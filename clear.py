#

import os

folders = ['Channel', 'Decoder', 'Encoder', 'Image', 'Output']
files_to_exclude = ['image_0.png', 'image_0.txt']

for folder_path in folders:
    if not os.path.isdir(folder_path):
        print(f"The path {folder_path} is not a directory or does not exist.")
        continue
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file not in files_to_exclude:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Removed file: {file_path}")
                except:
                    print(f"Failed to remove file {file_path}")