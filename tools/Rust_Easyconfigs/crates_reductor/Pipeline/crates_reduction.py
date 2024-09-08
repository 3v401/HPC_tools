import subprocess
import sys

# Files for parser.py (ends with .lock)
lock_files = [f for f in sys.argv[1:] if f.endswith('.lock')]

# Call parser.py with .lock files
if lock_files:
    try:
        subprocess.run(['python3', 'parser.py'] + lock_files, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred when calling parser.py: {e}")

# Call remove_duplicates.py with .txt files
if  True:
    try:
        subprocess.run(['python3', 'remove_duplicates.py', 'crates_list.txt'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred when calling remove_duplicates.py: {e}")

# Inform user that process is done
print("Reduction process completed.")

