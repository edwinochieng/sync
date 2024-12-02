import json
import os
from vcs.config import OBJECTS_DIR

def diff_commits(commit_hash1, commit_hash2):
    def get_commit_files(commit_hash):
        commit_path = f"{OBJECTS_DIR}/{commit_hash}"
        if not os.path.exists(commit_path):
            print(f"Commit {commit_hash} not found.")
            return {}
        with open(commit_path, "r") as commit_file:
            return json.load(commit_file)["files"]

    files1 = get_commit_files(commit_hash1)
    files2 = get_commit_files(commit_hash2)

    all_files = set(files1.keys()).union(set(files2.keys()))
    for file in all_files:
        if file not in files1:
            print(f"File {file} added in {commit_hash2}")
        elif file not in files2:
            print(f"File {file} removed in {commit_hash2}")
        elif files1[file] != files2[file]:
            print(f"File {file} modified in {commit_hash2}")
