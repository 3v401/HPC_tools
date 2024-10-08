import re
import argparse

def extract_lists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Beginning of first list:
    installed_packages_start = content.find("Installing collected packages:")
    # End of first list and beginning of the second list:
    installed_packages_end = content.find("Successfully installed")
    # Names of libraries
    installed_packages_text = content[installed_packages_start:installed_packages_end]

    # Names of libraries and versions
    successfully_installed_text = content[installed_packages_end:]

    #Extract the package names (without versions) from first list
    installed_packages = re.findall(r'([a-zA-Z0-9\-]+)', installed_packages_text.split("Installing collected packages:")[-1])

    # Extract the package names and versions from second list
    installed_versions = re.findall(r'([a-zA-Z0-9\-]+)-([0-9\.]+)', successfully_installed_text)

    # Create dictionary
    exts_list = {pkg: None for pkg in installed_packages}  # Initialize the dict with the package names
    
    # Update dictionary with versions from second list
    for pkg, version in installed_versions:
        if pkg in exts_list:
            exts_list[pkg] = version
    
    return exts_list

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Extract package names and versions from a text file.")
    parser.add_argument("file_path", type=str, help="Path to the input text file")

    args = parser.parse_args()

    exts_list = extract_lists(args.file_path)

    print("The exts_list required for the easyconfig is:")
    for key, value in exts_list.items():
        # If value has content
        if value:
            print(f"{key} {value}")

if __name__ == "__main__":
    main()
