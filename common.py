import subprocess
from os.path import expanduser


def execute_command(command):
    p = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
    output = p.communicate(0)
    output = output[0].decode('ascii')
    return output


def converted_path(path):
    return path.replace('~', expanduser("~"))
