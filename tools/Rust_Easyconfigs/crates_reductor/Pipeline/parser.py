import sys

# Check if at least one filename is provided
if len(sys.argv) < 2:
    print("Usage: python3 parser.py <path_to_file1> <path_to_file2> ...")
    sys.exit(1)  # Exit the script if no arguments are provided

crates = []  # Final list to store all crates from all files

# Loop over all provided filenames
for filename in sys.argv[1:]:
    try:
        with open(filename, 'r') as file:
            name = None
            version = None

            for line in file:
                line = line.strip()

                if line.startswith("name = "):
                    if '"' in line:
                        name = line.split('"')[1]
                
                if line.startswith("version = "):
                    if '"' in line:
                        version = line.split('"')[1]

                if name and version:
                    crates.append((name, version))
                    name = None
                    version = None

    except FileNotFoundError:
        print(f"File not found: {filename}")
        continue
    except Exception as e:
        print(f"Error processing file {filename}: {e}")
        continue

# Print the final list of crates
# print("crates = [")
# for crate in crates:
#     print(f"    ('{crate[0]}', '{crate[1]}'),")
# print("]")

# Save the final list of crates to "crates_list.txt"
output_file = "crates_list.txt"
with open(output_file, 'w') as f:
    f.write("crates = [\n")
    for crate in crates:
        f.write(f"    ('{crate[0]}', '{crate[1]}'),\n")
    f.write("]\n")

print(f"Final list of crates saved to '{output_file}'")

# Read and print the contents of "crates_list.txt" at the end of the program
with open(output_file, 'r') as f:
    print("\nContents of crates_list.txt:")
    print(f.read())
