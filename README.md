# Tools developed:

1. [Rust Version Compatibility Checker for Git Projects]()
2. [Rust Crates Reductor](https://github.com/3v401/HPC_tools/tree/main/tools/Rust_Easyconfigs/crates_reductor)
3. [Automate slurm jobs on several HPC systems at once](https://github.com/3v401/HPC_tools/tree/main/tools/autoslurmjob)
4. [Return pip installation list in order of installations with versions](https://github.com/3v401/HPC_tools/tree/main/tools/easyconfig_ext_list_settler)
5. [Interdependency versions checker in environment](https://github.com/3v401/HPC_tools/tree/main/tools/interdependency_checkers)
6. [Automated Kernel Builder](https://github.com/3v401/HPC_tools/tree/main/tools/kernel_builder)
7. [HPC Crawler]() TO DO: Create a tool that from a input.txt looks for all the extensions named 'word_row_i' to check if they are in the repo as an extension or module

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
Open remote shell on specific node `dc-gh` and setup easybuild:
```
salloc -p dc-gh -A <PROJECTNAME> -t 05:00:00 --chdir=/p/project1/<PROJECTNAME> /bin/sh
srun --pty /bin/bash --noprofile --norc
ml --force purge
unset $(env | grep EASYBUILD | cut -d= -f1)
env | grep EASYBUILD
source ~/gh200/setup.sh
```
Check queue of nodes:
```
squeue -p <NODENAME> -o "%.18i %.8u %.10M %.10l %.2t %.20R %.20b"
```
###### inodes (for disk-quota exceeded)
```
# Finds directories with most inodes in first level (faster than inodesDu)
inodesFind() {
  { find "$1" -xdev -printf '%h\n' | sort | uniq -c | sort -k 1 -n | tail -25; } 2>/dev/null
}
```
Apply: `inodesFind <PATH_TO_EXPLORE>`
###### extension versions in private repo
Retrieve available versions for python in a private repo:
```
python3 -m pip index versions <EXTENSION> --index-url https://token:<YOUR_TOKEN>@<PRIVATE_REPO_DOMAIN>/<PATH/TO/FILES>
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
Are sensitive files being tracked in history?
```
git ls-files | grep -E '\.pem$|\.tfstate$|\.auto\.tfvars$|\.key$|\.pub$'
```
##### Github
Open PR:
```
gh pr create \
  --repo <target_repository> \
  --base <target_branch> \
  --head <username>:<your_local_branch> \
  --title "{moduleclass}[toolchain] <name> v<version> " \
  --body "<Description>"
```

##### Crates generation. At root directory where Cargo.lock is located:
```
module load GCCcore/.13.3.0 Rust/1.78.0 Python-bundle-PyPI/2024.06
python -m easybuild.easyblocks.generic.cargo .
```
#### Terraform
Run a full module reinitialization.
```
terraform init -reconfigure -upgrade
terraform fmt -recursive
terraform validate
terraform apply
```
Run terraform with *.tfvars:
```
terraform plan -var-file=dev.tfvars
terraform apply -var-file=dev.tfvars
```
##### Lambdas
Convert .ts to .js for lambdas:
```
npx esbuild index.ts \
  --bundle \
  --platform=node \
  --target=node20 \
  --outfile=index.js
```
Convert .js to .zip
```
zip stripe-webhook-2024-12-30.1.zip index.js
```
Upload to S3:
```
aws s3 cp stripe-webhook-2024-12-30.1.zip \
  s3://path/to/upload/2024-12-30.1.zip
```
Check hash:
```
shasum -a 256 stripe-webhook-2024-12-30.1.zip
```
##### AWS
Get current user info
```
aws sts get-caller-identity
```
Check archives in S3:
```
aws s3 ls s3://path/to/check/
```
Remove archives in S3:
```
aws s3 rm s3://path/to/file/2024-12-30.1.zip
```
## Links/Sources

1. Docker cheatsheet CLI: [Link](https://docs.docker.com/get-started/docker_cheatsheet.pdf)
2. Dockerfile cheatsheet command [Link](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index)
