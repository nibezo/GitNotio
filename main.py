from github import Github
import private_token
# Open Notion page
# Parse Notion page, if there are changes
# Each Notion page = .md
# Update git repo, create files, if there are new Notion pages (new .md)

# using for access private_token.py
user = Github(private_token.token)
# Create a list with your repositories
repositories = [str(repo.full_name) for repo in user.get_user().get_repos()]

# Get user's login
login = user.get_user().login

# Create repo variable for
repo = user.get_repo(f'{login}/gitnotiotest')
contents = repo.get_contents('test.md', ref="test")

with open('Python/numpy.md', 'r') as file:
    data = file.read()
print(type(data))
repo.update_file(contents.path, "it's new `file change` commit", data, contents.sha, branch="test")
