import sys
from vcs.init import init_repo
from vcs.staging import add_to_index
from vcs.commit import commit_changes
from vcs.log import view_commit_history
from vcs.branching import create_branch,checkout_branch
from vcs.merging import merge_branches
from vcs.cloning import clone_repo
from vcs.diff import diff_commits
from vcs.init import init_repo
from vcs.ignore import ignore_file


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python main.py <command> [options]")
        return

    command = args[0]
    if command == "init":
        init_repo()
    elif command == "add" and len(args) > 1:
        add_to_index(args[1])
    elif command == "commit" and len(args) > 1:
        commit_changes(args[1])
    elif command == "log":
        view_commit_history()
    elif command == "branch" and len(args) > 1:
        create_branch(args[1])
    elif command == "checkout" and len(args) > 1:
        checkout_branch(args[1])
    elif command == "merge" and len(args) > 1:
        merge_branches(args[1])
    elif command == "diff" and len(args) > 2:
        diff_commits(args[1], args[2])
    elif command == "clone" and len(args) > 1:
        clone_repo(args[1])
    elif command == "ignore" and len(args) > 1:
        ignore_file(args[1])
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
