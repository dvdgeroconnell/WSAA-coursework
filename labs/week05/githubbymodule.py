# Program to use PyGithub to retrieve the URL of a file in a private repository
# and download the content.

# Author(s): David O'Connell, Andrew Beatty (Wk 5 lab 2)

import requests
import json
from github import Github
from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)
#print(type(g))
for repo in g.get_user().get_repos():
    #print(type(repo))
    print(repo.name)
    #print(repo)
    print(repo.clone_url)

myrepo = g.get_repo("dvdgeroconnell/WSAA-restricted")
print("Repo name:",myrepo.name, "  Clone URL:",myrepo.clone_url)

file_info = myrepo.get_contents("test1.txt")
url_of_file = file_info.download_url
print("URL of file is: ", url_of_file)
response = requests.get(url_of_file)
file_content = response.text
print(file_content)

# This is just to test that I can read a file in a folder in the repo.
# The only difference is the path.

file2_info = myrepo.get_contents("/test/test2.txt")
url_of_file2 = file2_info.download_url
print("URL of file is: ", url_of_file2)
response2 = requests.get(url_of_file2)
file2_content = response2.text
print(file2_content)

# Append some text to the file.
print("type is",type(file_content))
new_content = file_content + "more stuff. \n"
print(new_content)
github_response = repo.update_file(file_info.path, "updated by program", new_content, file_info.sha)
print(github_response)

g.close()
