import os
import sys


def _get_dir_base(file_info):
    if len(file_info['root']) == 0:
        dir_base = file_info['file_base']
    else:
        dir_base = '/'.join([file_info['root'], file_info['file_base']])
    return dir_base


def get_list_of_all_pdfs(path):
    '''
    Go through `path` and all its subdirectories and generate a list
    of dictionaries of the format:

    {'root': root, 
     'file': file, 
     'file_base': file without extension
     'dir_base': target directory}
    
    root is stripped of `path` by replacing it with a dot `.`
    '''
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pdf'):
                file_info = {}
                root = root.replace(path, '')
                if root.startswith('\\'):
                    root = root[1:]
                file_info['root'] = root.replace('\\','/')
                file_info['file'] = file
                file_info['file_base'] = os.path.splitext(file)[0]
                file_info['dir_base'] = _get_dir_base(file_info)
                file_list.append(file_info)
    return file_list
           
if __name__ == '__main__':
    print(get_list_of_all_pdfs(sys.argv[1]))