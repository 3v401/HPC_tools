venv list:

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
