Note:

This script must be run in HPC systems in a path close to easybuild-repository. Otherwise it won' t work because when looking for repo_extensions, it looks for a specific path. It won't work locally. It must be run on the cloud and logged.

venv list:

(Python part)

This code grabs the output of pip.
Saves in a column list by order of prompt the extensions after the sentence:
"Installing collected packages: "
saves in columns in order of appearance the following list:
texttable, fastjsonschema, websocket-client, webcolors, urllib3, uri-template,
Then grabs the next sentence:
"Successfully installed "
Looks for the first word in the previous list (i.e. texttable in this example) and searches for it in the next list
anyio-4.4.0 argon2-cffi-23.1.0 
when found, grabs the term "-X.X.X" and stores it in a dictionary {texttable: 'X.X.X'}
The returned column dictionary list is the venv list.


Repo list:

(Shell part)

Note: you must have the repository updated to the latest version. In the script insert fetch upstream, rebase, push
to be sure that you are with the latest version.

Access the repository remotes/upstream/2024. Launches a search command for each extension in the previous list/dictionary
('extension_name',
if extension_name found, find the part ,'version' and store "version" in an array or dictionary (extension1: version1, extension2: version2,...)
when the array is finished, move it to the python script as an input argument.
Check the previous dictionary, compare both dictionaries.
We have dictionary_repo with its extensions and dictionary_pip with its extensions (they do not have the same extensions necessarily).
Grab key1 from dictionary_pip and search for it in dictionary_repo:
  1. If found, store in dictionary_final {key1: value1, value2} where key1 is the extension_name and value1 value2 are the versions of dictionary_pip and dictionary_repo
     respectively
  2. If not found, store in dictionary_final {key1: value1} where key1 is the extension_name and value1 is the version of dictionary_pip
Run this for all elements in dictionary_pip. After all elements are checked, return the dictionary in columns like:

extension name: version pip venv, version Stages/2024
key1: value1, value2

key2: value1, value2

key3: value1

key4: value1

key5: value1, value2

...

keyn: value1

Count the number of keys in the dictionary such that value1!=value2. Those are the one which have incompatibility.
If:
keyn: value1==value2, no problem
keyn: value1, no problem
keyn: value1!=value2 incongruency

Prepare the code to ask for 4 outcomes:
input:
  1. all: return the complete dictionary in column format
  2. equal: return the dictionary in column format of keyn: value1==value2
  3. unique: return dictionary in column format for keyn: value1
  4. different: return dictionary in column format for keyn: value1!=value2

Also generate an output.txt with the following extructure (to introduce into an google sheets excel)

extension_name venv Stages/2024

key1            value1 value2

key2            value1 value2

key3            value1

key4            value1

...

keyn            value1
