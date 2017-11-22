'''
make_index.py
'''

import os
import re
from .pstring import pstring


def _sort_dir_then_files(root):
    fs = os.listdir(root)
    directory_list = [f for f in fs if os.path.isdir(os.path.join(root, f))]
    file_list = [f for f in fs if os.path.isfile(os.path.join(root, f))]
    return directory_list, file_list


def contains_html(root, file_list):
    for filename in file_list:
        filepath = os.path.join(root, filename)
        if filepath.endswith('.html'):
            return True
    return False


def extract_title_from_html(filename):
    with open(filename, 'r') as file:
        for line in file.readlines():
            result = re.match('.*<title>(.*)</title>.*', line)
            if result:
                return result.group(1)
    return ''


def parse_root(ps, root):
    directory_list = _sort_dir_then_files(root)[0]
    ps += '<ul>'
    for directory in directory_list:
        if directory not in ['png', 'css']:
            f = os.path.join(root, directory, directory) + '.html'
            if os.path.isfile(f):
                clean_filepath = f.replace('./html', '.')
                ps += '<li> <a href=\"{}\">{}</a> </li>'.format(clean_filepath, directory)
                title = extract_title_from_html(f)
                ps += '<li> {} </li>'.format(title)
            else:
                ps += '<li> {} </li>'.format(directory)
                parse_root(ps, os.path.join(root, directory))
    ps += '</ul>'
    return ps

def make_index():
    if os.path.isfile('./html/index.html'):
        os.remove('./html/index.html')

    ps = pstring()
    ps = parse_root(ps, './html')

    head = '<!doctype html><html><head>'
    head += '<link rel="stylesheet" type="text/css" href="./css/index.css">'
    head += '</head><body>'    
    tail = '</body></html>'
    s = head + ps._s + tail

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(s, 'html.parser')
    with open('./html/index.html','w') as f:
        f.write(soup.prettify())

if __name__ == '__main__':
    make_index()