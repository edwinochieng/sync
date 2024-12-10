import argparse
from vcs.init import init_repo
from vcs.staging import add_to_index
from vcs.commit import commit_changes
from vcs.log import view_commit_history
from vcs.branching import create_branch, checkout_branch
from vcs.merging import merge_branches
from vcs.cloning import clone_repo
from vcs.diff import diff_commits
from vcs.ignore import ignore_file

def main():
    parser = argparse.ArgumentParser(
        prog="sync",
        description="A lightweight distributed version control system",
    )
    
    # Define subparsers for each command
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init
    init_parser = subparsers.add_parser("init", help="Initialize a new repository")
    init_parser.set_defaults(func=lambda args: init_repo())

    # add
    add_parser = subparsers.add_parser("add", help="Add a file to the staging area")
    add_parser.add_argument("file", help="The file to stage")
    add_parser.set_defaults(func=lambda args: add_to_index(args.file))

    # commit
    commit_parser = subparsers.add_parser("commit", help="Commit staged changes")
    commit_parser.add_argument("-m", "--message", required=True, help="Commit message")
    commit_parser.set_defaults(func=lambda args: commit_changes(args.message))

    # log
    log_parser = subparsers.add_parser("log", help="View commit history")
    log_parser.set_defaults(func=lambda args: view_commit_history())

    # branch
    branch_parser = subparsers.add_parser("branch", help="Create a new branch")
    branch_parser.add_argument("branch_name", help="The name of the new branch")
    branch_parser.set_defaults(func=lambda args: create_branch(args.branch_name))

    # checkout
    checkout_parser = subparsers.add_parser("checkout", help="Switch to another branch")
    checkout_parser.add_argument("branch_name", help="The branch to switch to")
    checkout_parser.set_defaults(func=lambda args: checkout_branch(args.branch_name))

    # merge
    merge_parser = subparsers.add_parser("merge", help="Merge another branch into the current branch")
    merge_parser.add_argument("branch_name", help="The branch to merge into the current branch")
    merge_parser.set_defaults(func=lambda args: merge_branches(args.branch_name))

    # diff
    diff_parser = subparsers.add_parser("diff", help="Show differences between two commits")
    diff_parser.add_argument("commit1", help="The first commit to compare")
    diff_parser.add_argument("commit2", help="The second commit to compare")
    diff_parser.set_defaults(func=lambda args: diff_commits(args.commit1, args.commit2))

    # clone
    clone_parser = subparsers.add_parser("clone", help="Clone a repository")
    clone_parser.add_argument("destination", help="The destination directory for the cloned repository")
    clone_parser.set_defaults(func=lambda args: clone_repo(args.destination))

    # ignore
    ignore_parser = subparsers.add_parser("ignore", help="Add a file or pattern to the ignore list")
    ignore_parser.add_argument("pattern", help="The file or pattern to ignore")
    ignore_parser.set_defaults(func=lambda args: ignore_file(args.pattern))

    # Parse arguments and execute the appropriate function
    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
    else:
        try:
            args.func(args)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
