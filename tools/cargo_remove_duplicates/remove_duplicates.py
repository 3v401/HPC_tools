import sys
import ast

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
        for line in file:
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
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 remove_duplicates.py <path_to_file>")
        sys.exit(1)

    # Get the filename from the command-line argument
    filename = sys.argv[1]

    # Read the list of crates from the file
    crates = read_crates_from_file(filename)

    # Remove duplicates
    unique_crates = remove_duplicates(crates)

    # Print the unique crates
    print("crates = [")
    for crate in unique_crates:
        print(f"    {crate},")
    print("]")

if __name__ == "__main__":
    main()
