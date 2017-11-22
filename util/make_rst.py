'''
make_rst_and.py
'''

import os
from os.path import getmtime
import subprocess
import re
import sys
                
def initialize_rst(rst_file, png_list):
    def print_row(f, png_filename):
        f.write('.. {0} {1} {0}\n\n'.format('v'*20, png_filename))
        f.write('.. class:: row\n\n')
        f.write('   .. class:: left\n\n')
        f.write('   Readme\n\n')
        f.write('   .. class:: right\n\n')
        f.write('      .. image:: .\\png\\{0}\n\n'.format(png_filename))
            
    with open(rst_file, 'w') as f:
        f.write('==========\n')
        f.write('TITLE HERE\n')
        f.write('==========\n\n')
        f.write(':Authors: <author1>; <author2>;\n')
        f.write(':Date: <date here>\n\n')
        for png_filename in png_list:
            print_row(f, png_filename)

rst_file = sys.argv[1]
png_list = sys.argv[2:]
initialize_rst(rst_file, png_list)