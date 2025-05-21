import os
import subprocess
import sys

"""
In this snippet we are trying to answer:

Which is the newest tag in this project that builds with Rust {ver}?
"""

def run(cmd, quiet=False):
    """
    Run shell command helper function
    """
    try:
        # If quiet=True -> Run command and suppress all output
        if quiet:
            subprocess.run(
                cmd,                           # Shell command to run
                shell=True,                    # Run through bash
                stdout=subprocess.DEVNULL,     # Discard standard output prints
                stderr=subprocess.DEVNULL,     # Discard standard error prints
                check=True                     # Raise exception if command fails
            )
        else:
        # If quiet=False -> Run command and print all output
            subprocess.run(
                cmd,
                shell=True,
                check=True
            )
        # If command success, return True
        return True
    # If command fails, return False
    except subprocess.CalledProcessError:
        return False


def main():
    # First check if you are in a Rust project
    ver = input("Enter the Rust version you want to check: ")
    repo_url = input("Enter URL (.git) of repo to clone: ")
    repo_name = os.path.splitext(os.path.basename(repo_url))[0]

    print(f"Cloning repo {repo_url} into folder {repo_name}...")
    # Tell Rust to use version {ver} in the current directory
    # To ensure no accidental run of wrong Rust version during for loop
    if not run(f"git clone {repo_url}"):
        print("Failed to clone repo: \n", repo_url)
        sys.exit(1)

    # cd not valid as it is Python who need to change directory, not user shell:
    try:
        os.chdir(repo_name)
        print("Changed directory to: \n", os.getcwd())
    except FileNotFoundError:
        print("Failed to move into directory: \n", repo_name)

    if not os.path.exists("Cargo.toml"):
        print("Not in a Rust project directory.")
        sys.exit(1)

    print(f"Setting Rust override to {ver}...")
    # Tell Rust to use version {ver} in the current directory
    # To ensure no accidental run of wrong Rust version during for loop
    if not run(f"rustup override set {ver}"):
        print(f"Failed to set Rust version {ver}")
        sys.exit(1)

    # Get sorted tags from most recent to oldest
    print("Fetching Git tags...")
    result = subprocess.run("git tag --sort=-v:refname", shell=True, capture_output=True, text=True)
    tags = result.stdout.strip().splitlines()

    # If there are no tags:
    if not tags:
        print("No tags in this repo.")
        sys.exit(1)

    # List of compatible tags with Rust {ver}
    compatible = []

    for tag in tags:
        print(f" Checking tag: {tag}")
        if not run(f"git checkout -q {tag}", quiet = True):
            print(f"Failed to checkout tag: {tag}")
            continue

        if run("cargo check", quiet=True):
            print(f" Compatible with Rust {ver}: {tag}")
            compatible.append(tag)
        else:
            print(f"Not compatible: {tag}")

    if compatible:
        print(f"All compatible versions with Rust {ver}: \n", compatible)
        sys.exit(0)
    else:
        print(f"No compatible version of {repo_name} found for Rust {ver}.")
        sys.exit(1)

if __name__=="__main__":
    main()