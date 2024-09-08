This snippet takes as input a .txt file 'crates_list.txt' previously built in [crates_list.txt repository]. This file contains all the extensions needed for the Rust based repository. It grabs the name and version of each extension. If:
1. The name and version are the same, only saves one.
2. The name is the same and the version is different, saves both of them.
3. The name is different and the version is different, saves both of them.

The objective of this program is to remove all dependency duplicates and insert the 'crates' into the easyconfig file for later compilation.

This python program removes the duplicates obtained from cargo parser.py from this link.
(Explain what happens with qoqo-quest example)
