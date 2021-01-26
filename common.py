import subprocess
from os.path import expanduser
import os

import pdb


def execute_command(command):
    p = subprocess.Popen([command], shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')
    if len(error):
        return error
    return output


def converted_path(path):
    return path.replace('~', expanduser("~"))


def print_in_color(msg, color='none', end='\n'):
    color = color.upper()
    if(color == 'GREEN'):
        print("\033[92m {}\033[00m" .format(msg), end=end)
    elif(color == 'RED'):
        print("\033[91m {}\033[00m" .format(msg), end=end)
    elif(color == 'ORANGE'):
        print("\033[93m {}\033[00m" .format(msg), end=end)
    else:
        print("{}" .format(msg), end=end)


def check_for_local_and_unstaged_changes():
    output = execute_command('git status')
    if output.find('nothing to commit, working tree clean') > -1:
        print_in_color('NO STASH NEEDED', 'green')
        return False
    else:
        print_in_color('STASH NEEDED', 'red')
        return True


def stash_changes_and_perform_action(path, action=None):
    if not action:
        print_in_color('No Action Provided', 'red')
        return
    PATH = converted_path(path)
    os.chdir(PATH)
    changes = check_for_local_and_unstaged_changes()
    if(changes):
        branch = execute_command('git branch --show-current')
        execute_command('git stash')
        print_in_color(
            '## STASHED THE UNCOMMITED AND UNSTAGED CHANGES ##', 'green')
        action()
        execute_command('git checkout '+branch)
        execute_command('git stash pop')
        print_in_color(
            '## REVERTED TO ORIGINAL STATE (POPPED THE STASH) ##', 'green')
    else:
        branch = execute_command('git branch --show-current')
        action()
        execute_command('git checkout '+branch)


# os.chdir(os.getcwd())
# print(execute_command('git checkout alsjnc'))
