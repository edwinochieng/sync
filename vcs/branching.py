import os
from vcs.config import REFS_DIR,HEAD_FILE,OBJECTS_DIR
from vcs.commit import get_current_commit

def create_branch(branch_name):
    branch_path = f"{REFS_DIR}/{branch_name}"
    if os.path.exists(branch_path):
        print(f"Branch {branch_name} already exists.")
        return
    
    current_commit = get_current_commit()
    with open(branch_path, "w") as branch_file:
        branch_file.write(current_commit or "")
    
    print(f"Created branch {branch_name}")


def checkout_branch(target):
    
    branch_path = f"{REFS_DIR}/{target}"
    commit_hash = None

    # Check if the target is a branch
    if os.path.exists(branch_path):
        # Read the commit hash associated with the branch
        with open(branch_path, "r") as branch_file:
            commit_hash = branch_file.read().strip()

        # Update HEAD to point to the branch
        with open(HEAD_FILE, "w") as head_file:
            head_file.write(f"ref: {branch_path}")
        print(f"Switched to branch {target}")
    elif os.path.exists(f"{OBJECTS_DIR}/{target}"):  # Check if target is a valid commit hash
        commit_hash = target

        # Update HEAD to detach from any branch and point to the commit
        with open(HEAD_FILE, "w") as head_file:
            head_file.write(target)
        print(f"Checked out commit {target}")
    else:
        print(f"Error: Branch or commit {target} does not exist.")
        return

    # Update working directory (pseudo-code for now)
    update_working_directory(commit_hash)

def update_working_directory(commit_hash):
    """
    Updates the working directory to match the state of the specified commit.
    This would involve:
      - Reading the commit object
      - Extracting the files associated with the commit
      - Writing those files to the working directory

    :param commit_hash: The commit hash to check out.
    """
    print(f"Updating working directory to commit {commit_hash}")
   
