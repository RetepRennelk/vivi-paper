import os
import re
import sys
import subprocess
from configobj import ConfigObj

def _get_nr_of_pages(file):
    cmd = 'mutool info {0}'.format(file)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    pattern = 'Pages: (\d+)'
    for line in p.stdout.readlines():
        g = re.match(pattern, line.decode('utf-8'))
        if g:
            N_pages = int(g.group(1))
            return N_pages
    return -1

def _get_split_factor(ini_file):
    split_factor = 2
    if os.path.isfile(ini_file):
        config = ConfigObj(ini_file)
        split_factor = config.as_int('split-factor')
    return split_factor

file = sys.argv[1]
ini_file = '' if len(sys.argv)==2 else sys.argv[2]
N_pages = _get_nr_of_pages(file)
split_factor = _get_split_factor(ini_file)

str = ''
if N_pages > 0:
    for i in range(1,N_pages*split_factor+1):
        str += '{:03d}.png '.format(i)
sys.stdout.write(str)