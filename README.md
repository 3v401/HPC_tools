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
##### Git
Create new branch from commit X
```
git checkout -b <branch_name> <commit_ID>
```
Show logs in graphical way:
```
git log --oneline --graph --decorate --all
```

## Links/Sources

1. Docker cheatsheet CLI: [Link](https://docs.docker.com/get-started/docker_cheatsheet.pdf)
2. Dockerfile cheatsheet command [Link](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index)
