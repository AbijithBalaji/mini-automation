import time
import os
import shutil

def move_files(source_dir, destination_dir):
    if os.path.exists(source_dir):
        for file_name in os.listdir(source_dir):
            source = os.path.join(source_dir, file_name)
            destination = os.path.join(destination_dir, file_name)
            try:
                shutil.move(source, destination)
                print('File moved from', source, 'to', destination)
            except FileNotFoundError:
                print('File not found')
    else:
        print('Source directory not found')
#Change the path of source and destination directory according to your need 
source_dir = "/home/soul/Downloads/VideoDownloader/"
destination_dir = "/home/soul/Downloads/Templates"

while True:
    move_files(source_dir, destination_dir)
    #change the time based on your requirement
    time.sleep(15)

