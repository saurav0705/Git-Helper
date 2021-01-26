# STEPS TO FOLLOW:
# 1. git branch --show-current && git stash
# 2. git checkout [branch]
# 3. git pull origin [branch]
# 4. git stash pop

import os
from os.path import expanduser
from common import execute_command, converted_path, print_in_color, stash_changes_and_perform_action
import pdb

PATH = None


def pull_branches():
    while True:
        print_in_color(
            "Enter Branch You Want to pull (N to Exit) :: ", 'green', '')
        branch = input()
        if(branch.upper() == 'N'):
            return
        pull_branch(branch)


def pull_branch(branch):
    output = execute_command('git checkout '+branch)
    if output.find('error:') > -1:
        print_in_color("no branch exist for this name".upper(), 'red')
        return
    execute_command('git pull origin '+branch)
    print_in_color('succesfully pulled latest '.upper() +
                   branch + ' IN REPO', 'green')


def stash_changes_and_pull_branches(path):
    stash_changes_and_perform_action(path, pull_branches)
