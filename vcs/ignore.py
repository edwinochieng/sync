import json
import os
from pathlib import Path
from vcs.config import REPO_DIR, INDEX_FILE
from vcs.utils import hash_file

def should_ignore(file_path):
    ignore_file = ".ignore"
    if not os.path.exists(ignore_file):
        return False

    with open(ignore_file, "r") as f:
        ignored_patterns = f.read().splitlines()

    file_path = str(file_path)
    for pattern in ignored_patterns:
        if pattern in file_path:
            return True
    return False

def ignore_file(file_path):
    if not os.path.exists(REPO_DIR):
        print("No repository found. Please initialize one.")
        return
    
    file_path = Path(file_path).resolve()
    if should_ignore(file_path):
        print(f"Ignored {file_path}")
        return
    
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
