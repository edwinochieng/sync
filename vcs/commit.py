import os
import hashlib
import json
from vcs.config import REPO_DIR, INDEX_FILE, OBJECTS_DIR, HEAD_FILE, REFS_DIR

def commit_changes(message):
    if not os.path.exists(REPO_DIR):
        print("No repository found. Please initialize one.")
        return
    
    if not os.path.exists(INDEX_FILE):
        print("Nothing to commit.")
        return

    # Load staged files
    with open(INDEX_FILE, "r") as index:
        staged = json.load(index)
    
    commit = {
        "message": message,
        "parent": get_current_commit(),
        "files": staged,
    }
    commit_hash = hashlib.sha1(json.dumps(commit, sort_keys=True).encode()).hexdigest()
    with open(f"{OBJECTS_DIR}/{commit_hash}", "w") as obj_file:
        json.dump(commit, obj_file)
    
    # Update branch ref
    current_branch = get_current_branch()
    branch_path = os.path.join(REFS_DIR, current_branch)  
    os.makedirs(os.path.dirname(branch_path), exist_ok=True) 
    with open(branch_path, "w") as branch_file:
        branch_file.write(commit_hash)
    
    # Clear the index
    os.remove(INDEX_FILE)
    print(f"Committed changes with hash {commit_hash}")

def get_current_branch():
    with open(HEAD_FILE, "r") as head:
        return head.read().strip().split(": ")[1]

def get_current_commit():
    current_branch = get_current_branch()
    branch_path = os.path.join(REFS_DIR, current_branch)  
    if os.path.exists(branch_path):
        with open(branch_path, "r") as branch_file:
            return branch_file.read().strip()
    return None
