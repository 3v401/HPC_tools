import sys
import ast
import shutil
from datetime import datetime



def remove_duplicates(crates):
    # Use an ordered dictionary to maintain the order while removing duplicates
    seen = set()
    unique_crates = []
    for crate in crates:
        if crate not in seen:
            seen.add(crate)
            unique_crates.append(crate)
    return unique_crates

def read_crates_from_file(filename):
    crates = []
    with open(filename, 'r') as file:

        lines = file.readlines()

        # Ignore the first and last lines
        if len(lines) > 2:
            lines = lines[1:-1]
        else:
            print("The file doesn't have enough lines to ignore the first and last.")
            sys.exit(1)

        for line in lines:
            line = line.strip()
            if line:  # Ignore empty lines
                try:
                    crate = ast.literal_eval(line)
                    # Flatten the tuple if it was mistakenly wrapped in another tuple
                    if isinstance(crate, tuple) and len(crate) == 1 and isinstance(crate[0], tuple):
                        crate = crate[0]
                    crates.append(crate)
                except (SyntaxError, ValueError) as e:
                    print(f"Error parsing line: {line}\n{e}")
                    continue
    return crates

def main():

    # Get the crates_list.txt file
    filename = 'crates_list.txt'

    # Create a backup with a timestamp in the filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f"{filename}_backup_{timestamp}"

    # Copy the file to the backup location
    shutil.copy(filename, backup_file)

    print(f"Backup of '{filename}' saved as '{backup_file}'")

    # Read the list of crates from the file
    crates = read_crates_from_file(filename)

    # Remove duplicates
    unique_crates = remove_duplicates(crates)

    # Print the unique crates
    # print("crates = [")
    # for crate in unique_crates:
    #     print(f"    {crate},")
    # print("]")

    # Create an output filename for the reduced list
    output_file = f"reduced_{filename}"

    # Write the unique crates to the output file
    with open(output_file, 'w') as out_file:
        out_file.write("crates = [\n")
        for crate in unique_crates:
            out_file.write(f"    {crate},\n")
        out_file.write("]\n")

    print(f"Unique crates have been saved to '{output_file}'")

    # Print the content of the reduced file
    print("\nContent of the reduced file:")
    with open(output_file, 'r') as out_file:
        print(out_file.read())  # Print the entire content of the file

if __name__ == "__main__":
    main()

