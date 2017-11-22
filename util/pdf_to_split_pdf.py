'''
pdf_to_split_pdf.py split_file source_file ini_file

call to mutool poster -x
'''
import os
import sys
from configobj import ConfigObj

def get_split_factor(ini_file):
    split_factor = 2
    if os.path.isfile(ini_file):
        config = ConfigObj(ini_file)
        split_factor = config.as_int('split-factor')
    return split_factor

split_file   = sys.argv[1]
source_file  = sys.argv[2]
ini_file     = sys.argv[3] if len(sys.argv)>3 else ''
split_factor = get_split_factor(ini_file)

cmd = 'mutool poster -x {} {} {}'.format(split_factor, source_file, split_file)
os.system(cmd)