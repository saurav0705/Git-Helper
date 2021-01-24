# STEPS TO FOLLOW:
# 1. git branch --show-current && git stash
# 2. git checkout [branch]
# 3. git pull origin [branch]
# 4. git stash pop


import os
from os.path import expanduser
from common import execute_command, converted_path, print_in_color


PATH = None


def pull_branches():
    while True:
        branch = input("Enter Branch You Want to pull (N to Exit) :: ")
        if(branch.upper() == 'N'):
            return
        pull_branch(branch)


def pull_branch(branch):
    execute_command('git checkout '+branch)
    execute_command('git pull origin '+branch)


def stash_changes_and_pull_branches(path):
    PATH = converted_path(path)
    os.chdir(PATH)
    changes = check_for_local_and_unstaged_changes()
    if(changes):
        branch = execute_command('git branch --show-current')
        execute_command('git stash')
        print_in_color('STASHED THE CHANGES', 'green')
        pull_branches()
        execute_command('git checkout '+branch)
        execute_command('git stash pop')
        print_in_color('REVERTED TO ORIGINAL STATE', 'green')
    else:
        branch = execute_command('git branch --show-current')
        pull_branches()
        execute_command('git checkout '+branch)


def check_for_local_and_unstaged_changes():
    output = execute_command('git status')
    if output.find('nothing to commit, working tree clean') > -1:
        print_in_color('NO STASH NEEDED', 'green')
        return False
    else:
        print_in_color('STASH NEEDED', 'red')
        return True
