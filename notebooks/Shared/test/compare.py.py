# Databricks notebook source
from github import Github

# Authenticate to GitHub using a personal access token or OAuth token
# Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your actual token
g = Github('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')

# Specify the repository name and owner
repo_owner = 'VarunKumar2690'
repo_name = 'DataOps'

# Get the repository object
repo = g.get_user(repo_owner).get_repo(repo_name)

# Specify the branch names
dev_branch_name = 'dev'
prod_branch_name = 'main'

# Get the branch objects
dev_branch = repo.get_branch(dev_branch_name)
prod_branch = repo.get_branch(prod_branch_name)

# Create a merge commit to merge the Dev branch into the Prod branch
merge_commit = repo.merge(base=prod_branch_name, head=dev_branch_name, commit_message='Merge Dev into Prod')

# Print the merge commit details
print(f"Merge Commit: {merge_commit.sha}")
print(f"Merge Commit Message: {merge_commit.commit.message}")
print(f"Merge Commit Author: {merge_commit.commit.author.name}")
print(f"Merge Commit Date: {merge_commit.commit.author.date}")

# Optionally, delete the Dev branch after successful merge
# dev_branch.delete()


# COMMAND ----------

import subprocess

# Change to the desired directory
new_dir = "DataOps"
subprocess.run(["cd", new_dir], shell=True)

# Run code or commands in the new directory
# For example, you can run a Python script using the `python` command
subprocess.run(["git", "pull", "origin", "main"], shell=True)
subprocess.run(["git", "pull", "origin", "dev"], shell=True)
