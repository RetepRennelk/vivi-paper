'''
get_path_to_style_css path1/path2/file.ext

returns ..\\..\\..\\util\\styles.css
'''
import os
import sys
import re

path, filename = os.path.split(sys.argv[1])
path_elements = re.split('/|\\\\', path)
str = '{0}css\\style.css'.format('..\\'*(len(path_elements)-2))
print(str)
