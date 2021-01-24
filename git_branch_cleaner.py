from common import execute_command, converted_path, print_in_color
import sys
import os
import subprocess
path = sys.argv

BRANCHES_TO_BE_SPARED = ['master', 'production']


def delete_these_branches(branches):
    for branch in branches:
        print_in_color(
            execute_command('git branch -D ' + branch), 'red')


def get_all_git_branches(path):
    os.chdir(converted_path(path))
    output = execute_command('git branch')
    branches = output.replace('*', '')
    for branch in BRANCHES_TO_BE_SPARED:
        branches = branches.replace(" "+branch+"\n", '')
    BRANCHES_TO_BE_DELETED = list(filter(lambda item: len(item) != 0, map(
        lambda item: item.strip(), branches.split('\n'))))
    if(len(BRANCHES_TO_BE_DELETED) == 0):
        print_in_color("No branch To Delete", 'green')
        print_in_color("PROTECTED BRANCHES :: ", 'green', '')
        print_in_color(BRANCHES_TO_BE_SPARED, 'orange')
    else:
        print_in_color(
            "Are You Sure You Want To delete These Branches ? ::  ", 'orange', '')
        print_in_color(BRANCHES_TO_BE_DELETED, 'red')
        answer = input("Enter Y To Delete :: ")
        if(answer.upper() == 'Y'):
            print_in_color("DELETING....", 'green')
            delete_these_branches(BRANCHES_TO_BE_DELETED)
        else:
            print_in_color("CANCELLED THE OPERATION", 'red')


if len(path) == 1:
    print("No path found")
else:
    get_all_git_branches(path[1])
