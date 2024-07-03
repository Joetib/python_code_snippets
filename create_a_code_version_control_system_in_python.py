# Use gitpython library to interact with git repositories
# >> pip install gitpython

from git import Repo

# Initialize a new git repository
repo = Repo.init('my_project')
# Create a new file
with open('my_project/file.txt', 'w') as file:
    file.write('Hello, World!')
# Add the file to the staging area
repo.index.add(['file.txt'])
# Commit the changes
repo.index.commit('Initial commit')
commits = list(repo.iter_commits())
for commit in commits:
    print(commit) # print commit log
# Output
# >> commit 1234567890abcdef1234567890abcdef1234567
# >> Author: John Doe <johndoe@example.com>
# >> Date:   Mon Sep 20 12:00:00 2021 +0000
# >> 
# >> Initial commit
# Please Like and Subscribe