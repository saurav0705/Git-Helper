import subprocess
from os.path import expanduser


def execute_command(command):
    p = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
    output = p.communicate(0)
    output = output[0].decode('ascii')
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
