When developing a Rust-based easyconfig for HPC systems with easybuild, there is a parameter that is very time consuming. That is the 'crates' parameter. Usually a repository contains several 'crates', for example 'maturin' or 'qoqo-quest'.

For this repository use as example the 'qoqo-quest' module to retrieve such 'crates' extensions. This is a very convinient example because the repository contains 468 extensions from which only 293 are unique. How to find the unique extension names and versions in an automated way? For that is 'crates_reductor'. This repository:

1. Takes as input all .lock files that 'qoqo-quest' repository needs and saves its crates extensions into a .txt file
2. Opens 'crates_list.txt' file and removes duplicates. This second step:
3. Prompts reduced crates list. Reduced the number of Rust extension calls from 468 to 293.
