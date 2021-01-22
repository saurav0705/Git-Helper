# STEPS TO FOLLOW:
# 1. git branch --show-current && git stash
# 2. git checkout master
# 3. git pull origin master
# 4. git checkout production
# 5. git pull origin production


import os
from os.path import expanduser
from common import execute_command, converted_path


def check_for_local_and_unstaged_changes(path):
    path = '~/Desktop/Flipkart/sp-harmony/sp-harmony-metrics'
    path = '~/Desktop/Flipkart/sample'
    os.chdir(converted_path(path))
    output = execute_command('git status')
    if output.find('nothing to commit, working tree clean') > -1:
        print('NO STASH NEEDED')
    else:
        print('STASH NEEDED')


check_for_local_and_unstaged_changes('dac')
