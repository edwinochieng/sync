import json
import os
import hashlib
from vcs.config import OBJECTS_DIR, REFS_DIR
from vcs.commit import get_current_commit,get_current_branch


def merge_branches(branch_name):
    branch_path = f"{REFS_DIR}/{branch_name}"
    if not os.path.exists(branch_path):
        print(f"Branch {branch_name} does not exist.")
        return

    with open(branch_path, "r") as branch_file:
        branch_commit = branch_file.read().strip()
    current_commit = get_current_commit()

    if not branch_commit or not current_commit:
        print("Cannot merge, one of the branches has no commits.")
        return

    # Detect conflicts
    with open(f"{OBJECTS_DIR}/{branch_commit}", "r") as branch_obj:
        branch_files = json.load(branch_obj)["files"]
    with open(f"{OBJECTS_DIR}/{current_commit}", "r") as current_obj:
        current_files = json.load(current_obj)["files"]

    conflicts = []
    merged_files = current_files.copy()
    for file, hash in branch_files.items():
        if file in current_files and current_files[file] != hash:
            conflicts.append(file)
        else:
            merged_files[file] = hash

    if conflicts:
        print(f"Merge conflicts detected in files: {', '.join(conflicts)}")
        return

    # Create merge commit
    commit = {
        "message": f"Merge branch {branch_name} into current branch",
        "parent": current_commit,
        "files": merged_files,
    }
    commit_hash = hashlib.sha1(json.dumps(commit, sort_keys=True).encode()).hexdigest()
    with open(f"{OBJECTS_DIR}/{commit_hash}", "w") as obj_file:
        json.dump(commit, obj_file)

    # Update current branch
    current_branch = get_current_branch()
    with open(f"{REFS_DIR}/{current_branch}", "w") as branch_file:
        branch_file.write(commit_hash)

    print(f"Branch {branch_name} merged successfully.")
