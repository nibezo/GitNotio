from github import Github
import private_token
# First create a Github instance:

# using an access private_token.py
g = Github(private_token.token)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
