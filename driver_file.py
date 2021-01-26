import cmd
import pathlib
import os
from os.path import expanduser
from common import converted_path
from git_pull_latest import stash_changes_and_pull_branches
from git_branch_cleaner import get_all_git_branches


class GitHelper(cmd.Cmd):
    path = os.getcwd()
    intro = 'Welcome to the Git Helper Shell. Type ? for help'
    prompt = '(Git Helper) $ '

    def check_path(self, path):
        return os.path.exists(converted_path(path))

    def do_set_path(self, path):
        'Set Path Of the git repor you want to perform actions : Example set_path <Path>'
        if path.upper() == 'SELF':
            self.path = os.getcwd()
            return

        if self.check_path(path):
            self.path = path
        else:
            print("Path Don't Exist")

    def do_get_path(self, line):
        'Returns Path for the Taget Repo'
        print(self.path)

    def do_pull_branch(self, line):
        'Pulls Latest of those branches in your current repo that you enter :  Example pull_branch'
        stash_changes_and_pull_branches(self.path)

    def do_clean_repo(self, line):
        'Cleans Repo of the extra branches other than protected branches'
        get_all_git_branches(self.path)

    def do_bye(self, arg):
        'Stop Git Helper, close the Git Helper window, and exit:  BYE'
        print('Thank you for using Git Helper')
        return True


if __name__ == '__main__':
    GitHelper().cmdloop()
