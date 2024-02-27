# assignment04-github.py
# Topic 05 Assignment

# Program to use PyGithub to read a file from a repository, replace all instances of the text "Andrew"
# with my name, commit the changes and push the file back to the repository.

# Author(s): David O'Connell

# Reference(s):
#    Andrew Beatty - WSAA5.2 Github API and WSAA5.3 Packages (video lectures & associated labs)
#    PyGithub Documentation: https://pygithub.readthedocs.io/en/latest/examples/Repository.html#
#    Handling base64 data in Python: https://www.askpython.com/python/examples/decoding-base64-data
# -----------------------------------------------------------------------------------------------------

# Use PyGithub
from github import Github

# Retrieve the Github token from the config.py file
from config import config as cfg

# Use the fine grained token generated in Github, with commit and content set to read / write
apikey = cfg["courseworkkey"]
g = Github(apikey)

# Get the content of the file
repo = g.get_repo("dvdgeroconnell/WSAA-coursework")
contents = repo.get_contents("assignments/assignment04.txt")

# Decode the byte encoded contents.decoded_content... found this by trial and error
internal_str = contents.decoded_content
internal_str = internal_str.decode("utf-8")
print("decoded downloaded file content\n", internal_str,sep='')

# Update all instances of "Andrew" in the file content
updated_content = internal_str.replace("Andrew", "Dave")
print("updated file content for upload\n", updated_content,sep='')

# Now push the modified content with appropriate commit message
update_str = "Updated by Assignment 04 program"
response = repo.update_file(contents.path, update_str, updated_content, contents.sha)
print(response)

# Tidy up
g.close()
