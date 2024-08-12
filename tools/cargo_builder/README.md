creates an easyconfig file with the following parameters:
name, version, URL...
calls the functions:
1. parser.py to obtain the crates
2. remove_duplicates.py to remove duplicates
3. inject--checksums to obtain checksums
4. sha.py to convert checksums in its corresponding format
