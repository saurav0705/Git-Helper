import cmd
import pathlib
import os
from os.path import expanduser
from common import converted_path


class GitHelper(cmd.Cmd):
    path = None

    def check_path(self, path):
        return os.path.exists(converted_path(path))

    def do_greet(self, line):
        print("hello")

    def do_set_path(self, path):
        if self.check_path(path):
            self.path = path
        else:
            print("Path Don't Exist")

    def do_global_path(self, line):
        print(self.path)

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    GitHelper().cmdloop()
