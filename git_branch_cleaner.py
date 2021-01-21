import sys
import os
import subprocess
import pprint
path = sys.argv
pp = pprint.PrettyPrinter(indent=4)

BRANCHES_TO_BE_SPARED = ['master', 'production']


def delete_these_branches(branches):
    command = ''
    for branch in branches:
        os.system('git branch -D ' + branch)


def get_all_git_branches(path):
    os.chdir(path)
    cmd = ['git branch']
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = p.communicate(0)
    output = output[0].decode('ascii')
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
            print("CANCELLED THE OPERATION")


if len(path) == 1:
    print("No path found")
else:
    get_all_git_branches(path[1])
