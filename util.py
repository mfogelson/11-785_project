import os
from pathlib import Path
from typing import List

def create_directories(folder_paths: List[Path]):
    # create create_directories if it does not exist
    for folder_path in folder_paths:
        if not os.path.exists(folder_path):
            print(f"'{folder_path}' directory does not exist...creating")
            os.makedirs(folder_path)
        else:
            print(f"'{folder_path}' directory already exists as a directory")
