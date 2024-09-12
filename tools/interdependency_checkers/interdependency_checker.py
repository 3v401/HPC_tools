"""

interdependency_checker:

This code takes as input x modules and checks all its 'packages'.
You can introduce as many modules as you want to.
Example:

        Input: module1, module2, module3
        Instruction 1: See the modules that share same package with DIFERENT version.
        Intruction 2: See the modules that share the same package with SAME version.
        Instruction 3: See the modules that share DIFFERENT package name.
        Returns the structure:

        package: {'module1': 'version1', 'module2': 'version2', 'module3': 'version3'}
"""

import sys


print("#####################################\n")
print("Welcome to the 'Interdependency checker'. This program checks all the modules that share the SAME or DIFFERENT package name.\n")
print("#####################################\n")

# Prompt user for input
module_path = []
while True:
    file_path = input("Enter the path to a module.txt file (leave blank to finish): ")
    if not file_path:
        break
    module_path.append(file_path)
    
instruction = input("\n Press 1 if you want to see the modules that share SAME package name with DIFERENT version.\n Press 2 if you want to see the modules that share the SAME package name with SAME version. \n Press 3 if you want to see modules that share DIFFERENT package name: ")

if instruction != '1' and instruction!= '2' and instruction!= '3':
        print("You introduced an incorrect keyword. Try again.")
        sys.exit(1)

print("Your selected intruction is: ", instruction)

# Get module names
module_names = []
for path in module_path:
    # Split the path by "/"
    parts = path.split('/')
    # Get the last part (which is the module name)
    module_name = parts[-1]
    # Remove any leading or trailing whitespace and append to module_names list
    module_names.append(module_name.strip())
    
# Print the extracted module names
print("Your introduced modules are: ") 
for i, module_name in enumerate(module_names, start=1):
    print(f"module{i} = {module_name}")



def read_module_file(file_name):
    package_versions = {}
    with open(file_name, 'r') as f:
        next(f)  # Skip header line
        next(f)  # Skip the '-----' that 'pip list' command does
        for line in f:
            if line.strip():  # Ensure line is not empty
                parts = line.split()
                if len(parts) >= 2:
                    package_name = parts[0].strip()
                    version = parts[1].strip()
                    package_versions[package_name] = version
    return package_versions

def create_comparison_dict(module_path, module_names):
    comparison_dict = {}
    
    for module_file, module_name in zip(module_path, module_names):
        module_data = read_module_file(module_file)
        for package, version in module_data.items():
            if package not in comparison_dict:
                comparison_dict[package] = {}
            comparison_dict[package][module_name] = version
    
    return comparison_dict

# If you want to check what zip does uncomment the following line:
# print(list(zip(module_path, module_names)))
# returns: [[('/path/to/module1', 'module1'), ('/path/to/module2', 'module2'), ('/path/to/module3', 'module3')]

# Create comparison dictionary
comparison_dict = create_comparison_dict(module_path, module_names)
    
    
if instruction == '1':
    print("You selected: modules that share SAME package name with DIFFERENT version.")
    for package, versions in comparison_dict.items():
        if len(set(versions.values())) > 1 and len(set(versions.keys())) != 1:
            # set: removes duplicates
            # If the number of duplicates is > 1 in version.values() -> Versions are not the same
            # If the number of duplicates is != 1 in version.keys() -> There is more than one module that uses this package
            print(f"{package}: {versions}")
elif instruction == '2':
    print("You selected: modules that share the SAME package name with SAME version.")
    for package, versions in comparison_dict.items():
        if len(set(versions.values())) == 1 and len(set(versions.keys())) != 1:
            # If the number of duplicates is == 1 in version.values() -> Versions are the same
            # If the number of duplicates is != 1 in version.keys() -> There is more than one module that uses this package
            print(f"{package}: {versions}")
elif instruction == '3':
    print("You selected: modules that share DIFFERENT package name.")
    for package, versions in comparison_dict.items():
        if len(versions) == 1:  # The package is only present in one module
            # Get the module name and version
            for module_name, version in versions.items():
                print(f"{package}: {{'{module_name}': '{version}'}}")
