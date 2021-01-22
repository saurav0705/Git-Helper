from common import execute_command, converted_path
import sys
import os
import subprocess
path = sys.argv

BRANCHES_TO_BE_SPARED = ['master', 'production']


def delete_these_branches(branches):
    for branch in branches:
        print("\033[91m {}\033[00m".format(
            execute_command('git branch -D ' + branch)))


def get_all_git_branches(path):
    os.chdir(converted_path(path))
    output = execute_command('git branch')
    branches = output.replace('*', '')
    for branch in BRANCHES_TO_BE_SPARED:
        branches = branches.replace(" "+branch+"\n", '')
    BRANCHES_TO_BE_DELETED = list(filter(lambda item: len(item) != 0, map(
        lambda item: item.strip(), branches.split('\n'))))
    if(len(BRANCHES_TO_BE_DELETED) == 0):
        print("No branch To Delete")
        print("\033[92m {}\033[00m \033[93m {}\033[00m" .format(
            "PROTECTED BRANCHES :: ", BRANCHES_TO_BE_SPARED))
    else:
        print("\033[92m {}\033[00m \033[91m {}\033[00m" .format(
            "Are You Sure You Want To delete These Branches ? ::  ", BRANCHES_TO_BE_DELETED))
        answer = input("Enter Yes To Delete :: ")
        if(answer.upper() == 'YES'):
            print("\033[93m {}\033[00m".format("DELETING...."))
            delete_these_branches(BRANCHES_TO_BE_DELETED)
        else:
            print("\033[91m {}\033[00m" .format("CANCELLED THE OPERATION"))


if len(path) == 1:
    print("No path found")
else:
    get_all_git_branches(path[1])
