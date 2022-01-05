from github import Github
import private_token
from notion2md.exporter import block_exporter

# First create a Github instance:

# using an access private_token.py
g = Github(private_token.token)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

#output_path is optional

block_exporter("https://www.notion.so/nibezo/test-8da692129af94b5da1810bd34ac13a2e")
