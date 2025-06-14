# Tools developed:

1. [Rust Version Compatibility Checker for Git Projects]()
2. [Rust Crates Reductor](https://github.com/3v401/HPC_tools/tree/main/tools/Rust_Easyconfigs/crates_reductor)
3. [Automate slurm jobs on several HPC systems at once](https://github.com/3v401/HPC_tools/tree/main/tools/autoslurmjob)
4. [Return pip installation list in order of installations with versions](https://github.com/3v401/HPC_tools/tree/main/tools/easyconfig_ext_list_settler)
5. [Interdependency versions checker in environment](https://github.com/3v401/HPC_tools/tree/main/tools/interdependency_checkers)
6. [Automated Kernel Builder](https://github.com/3v401/HPC_tools/tree/main/tools/kernel_builder)

#### Useful commands:

```
du -ah ~ | sort -rh | head -n 20
```
###### To obtain the SHA256 checksum of a file:
```
sha256sum <filename>
```
###### Find a file named filename:
```
find  $PATH -type f -name "*<filename>*"
```
###### Look for files in a $PATH named filename with a specific keyword inside:
```
find $PATH -type f -name "*<filename>*" -exec grep --with-filename "*<keyword>*" {} +
```
###### Look for files in a $PATH that contain a specific keyword inside:
```
find $PATH -type f -exec grep --with-filename "*<keyword>*" {} +
```
###### Patch creation:
```
diff -u <filename1> <filename2> > my_new_patch.patch
```
###### Patch that creates files from null:
```
cat <<EOF > <filename>
<content of file>
EOF
```
```
diff -u /dev/null <filename> > my_new_patch.patch
```
Bring file from other branch:
```
git checkout <branch_name> -- path/to/file
git add path/to/file
```
Agree with many file modifications/delets/addings in one command:
```
git add -u
git commit -m "Your commit comment"
```
###### inodes (for disk-quota exceeded)
```
# Finds directories with most inodes in first level (faster than inodesDu)
inodesFind() {
  { find "$1" -xdev -printf '%h\n' | sort | uniq -c | sort -k 1 -n | tail -25; } 2>/dev/null
}
```
Apply: `inodesFind <PATH_TO_EXPLORE>`
##### Git
Create new branch from commit X
```
git checkout -b <branch_name> <commit_ID>
```
Show logs in graphical way:
```
git log --oneline --graph --decorate --all
```
Are sensitive files being tracked in history?
```
git ls-files | grep -E '\.pem$|\.tfstate$|\.auto\.tfvars$|\.key$|\.pub$'
```

## Links/Sources

1. Docker cheatsheet CLI: [Link](https://docs.docker.com/get-started/docker_cheatsheet.pdf)
2. Dockerfile cheatsheet command [Link](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index)
