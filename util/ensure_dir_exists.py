import os
import sys

def ensure_dir_exists(path):
    if not(os.path.isdir(path)):
        os.makedirs(path)
        
if __name__ == '__main__':
    path = sys.argv[1]
    ensure_dir_exists(path)