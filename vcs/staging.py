import os
import hashlib
import json
from pathlib import Path
from vcs.config import REPO_DIR,INDEX_FILE

def hash_file(file_path):
    hasher = hashlib.sha1()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def add_to_index(file_path):
    if not os.path.exists(REPO_DIR):
        print("No repository found. Please initialize one.")
        return
    
    file_path = Path(file_path).resolve()
    if not file_path.exists():
        print(f"File {file_path} does not exist.")
        return
    
    file_hash = hash_file(file_path)
    staged = {}
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as index:
            staged = json.load(index)
    
    staged[str(file_path)] = file_hash
    with open(INDEX_FILE, "w") as index:
        json.dump(staged, index)
    
    print(f"Added {file_path} to index.")
