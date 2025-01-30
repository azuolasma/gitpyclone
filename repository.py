import os

from file_handling import write_file

def init(repo):
    # Create the repo folder inside current directory and inside it create .git folder
    os.makedirs(repo, exist_ok=True)
    os.makedirs(os.path.join(repo, ".git"), exist_ok=True)

    # Create the necessary subdirectories inside .git folder
    os.makedirs(os.path.join(repo, ".git", "objects"), exist_ok=True)
    os.makedirs(os.path.join(repo, ".git", "refs", "heads"), exist_ok=True)

    # Write the initial HEAD file
    write_file(os.path.join(repo, ".git", "HEAD"), b"ref: refs/heads/master")

    print(f"initialized empty Git repository: {repo}")