crates = []

with open('Cargo.lock', 'r') as file: 
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

print("crates = [")
for crate in crates:
    print(f"    ('{crate[0]}', '{crate[1]}'),")
print("]")
