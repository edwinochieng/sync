import json
from vcs.config import OBJECTS_DIR
from vcs.commit import get_current_commit

def view_commit_history():
    current_commit = get_current_commit()
    if not current_commit:
        print("No commits yet.")
        return
    
    while current_commit:
        with open(f"{OBJECTS_DIR}/{current_commit}", "r") as obj_file:
            commit = json.load(obj_file)
        print(f"Commit: {current_commit}")
        print(f"Message: {commit['message']}")
        print()
        current_commit = commit["parent"]
