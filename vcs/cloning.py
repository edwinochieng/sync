import os
import shutil
from pathlib import Path
from vcs.config import REPO_DIR

def clone_repo(destination):
    if not os.path.exists(REPO_DIR):
        print("No repository found to clone.")
        return
    destination_path = Path(destination).resolve()
    if os.path.exists(destination_path):
        print(f"Destination {destination} already exists.")
        return

    shutil.copytree(REPO_DIR, destination_path / REPO_DIR)
    print(f"Repository cloned to {destination_path}")


