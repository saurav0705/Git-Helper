from common import execute_command, converted_path, print_in_color
import sys
import os
import subprocess


BRANCHES_TO_BE_SPARED = []


def delete_these_branches(branches):
    print_in_color("Started Deleting Operation", 'green')
    for branch in branches:
        output = execute_command('git branch -D ' + branch)
        if "error" in output:
            print_in_color(
                output, 'red', "")
        else:
            print_in_color(
                output, 'orange', "")
    print_in_color("Completed Deleting Operation", 'green')


def delete_feature_branches(path, protected_branches):
    os.chdir(converted_path(path))
    output = execute_command('git branch')
    branches = output.replace('*', '')
    BRANCHES_TO_BE_SPARED = protected_branches
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
        print_in_color("Enter Y To Delete :: ", 'green', '')
        answer = input()
        if(answer.upper() == 'Y'):
            delete_these_branches(BRANCHES_TO_BE_DELETED)
        else:
            print_in_color("CANCELLED THE OPERATION", 'red')
