from github import Github
import private_token

# using an access private_token.py
user = Github(private_token.token)
# Create a list with your repositories
repositories = [str(repo.full_name) for repo in user.get_user().get_repos()]

# Get user's login
login = user.get_user().login

# Create repo variable for
repo = user.get_repo(f'{login}/gitnotiotest')

# repo.create_file('test.md', '`hello!`', 'is it a commit?', branch='test')
