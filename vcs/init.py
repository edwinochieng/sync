import os
from vcs.config import REPO_DIR, OBJECTS_DIR, REFS_DIR, HEAD_FILE

def init_repo():
    if os.path.exists(REPO_DIR):
        print("Repository already initialized.")
        return
    os.makedirs(OBJECTS_DIR)
    os.makedirs(REFS_DIR)
    with open(HEAD_FILE, "w") as head:
        head.write("ref: refs/heads/main\n")
    with open(f"{REFS_DIR}/main", "w") as main_branch:
        main_branch.write("")
    print(f"Initialized empty repository in {os.getcwd()}/{REPO_DIR}")
