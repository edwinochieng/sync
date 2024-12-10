# Sync

A lightweight distributed version control system implemented in Python. It is designed to be minimalist, focusing on the core concepts of version control.

## Features

- **Initialization**: Create a new repository.
- **File Staging**: Add files to the staging area.
- **Committing Changes**: Commit staged changes with a message.
- **Viewing Commit History**: View the commit log.
- **Branch Management**: Create and switch between branches.
- **Merging**: Merge branches.
- **File Diff**: View differences between commits.
- **Repository Cloning**: Clone repositories.
- **Ignoring Files**: Ignore files using a .ignore file.

## Requirements

- Python 3.8 or higher
- Pip package manager

## Installation

1. **Step 1: Clone the repository:**

   ```bash
   git clone https://github.com/edwinochieng/sync.git
   cd sync
   ```

2. **Set up a virtual environment:**

   Run the following command to create a virtual environment:

   ```bash
   python -m venv venv
   ```

   Then, activate the virtual environment.

   - On **mac/Linux**, run:

   ```bash
   source venv/bin/activate
   ```

   - On **Windows**, run:

   ```bash
   venv\bin\activate
   ```

3. **Step 3: Install the package in editable mode**

   ```bash
   pip install -e .
   ```

## Usage

After installation, you can use the custom sync commands from your terminal to perform version control actions.

### Available commands

- `sync init`: Initialize a new repository
- `sync add <file>`: Add a file to the staging area.
- `sync commit -m <message>`: Commit staged changes with a message.
- `sync log`: View commit history.
- `sync branch <branch-name>`: Create a new branch.
- `sync checkout <branch-name>`: Checkout an existing branch.
- `sync merge <branch-name>`: Merge the specified branch into the current branch.
- `sync diff <commit1> <commit2>`: View the diff between two commits.
- `sync clone <destination-path>`: Clone a repository.
- `sync ignore <file>`: Add a file to the .ignore list.

### Examples

**1. Initialize a Repository**

```bash
sync init
```

This creates a new version control repository in the current directory.

**2. Add a file to the staging**

```bash
sync add examples/file1.txt
```

This adds `file1.txt` to the staging area, preparing it for commit.

**3. Commit changes to the repository**

```bash
sync commit -m "Initial commit"
```

This commits the staged files with the provided message.

**4. View commit history**

```bash
sync log
```

Displays the commit history, showing each commit with details such as commit ID and message.

**5. Create a new branch**

```bash
sync branch new-feature
```

This creates a new branch called `new-feature`.

**6. Switch to a different branch**

```bash
sync checkout new-feature
```

This switches from the current working branch to the branch called `new-feature` branch.

**7. Merge a branch into the current branch**

```bash
sync merge new-feature
```

This merges the `new-feature` branch into the current branch.

**8. View the difference between two commits**

```bash
sync diff abc123 def456

```

This compares changes made between the two specified commits.

**9. Clone a Repository**

```bash
sync clone ../cloned-repo

```

This clones the repository into the specified directory.

**10. Ignore a file**

```bash
sync ignore secret.txt

```

This adds `secret.txt` file to the ignore list, meaning it will not be tracked by version control.

## Limitations

- **Merge Conflicts**: Merge conflicts must be resolved manually, as there is no automated conflict resolution.
- **No Remote Support**: The system only supports local disk cloning and does not work with remote repositories.
- **Basic Diff Implementation**: Diff functionality is limited to showing textual changes without advanced features like word-level or side-by-side diffs.
- **No Branch Merging Strategy**: Merge operations assume simple linear merges and do not handle complex merging strategies (e.g., rebase, fast-forward).
- **No File Locking**: There is no support for file locking, meaning concurrent changes to the same file can cause issues without proper coordination.
- **Limited Commit History**: The system stores basic commit history, but lacks advanced features like commit tagging or branching history visualization.
- **No Staging Area**: Files added to the staging area are immediately prepared for commit without an explicit “unstage” option.
