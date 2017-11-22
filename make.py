import os
import click
from util.get_list_of_all_pdfs import get_list_of_all_pdfs
from util.render_template import render_template
from util.make import Make
from util.make_index import make_index
from util.ensure_dir_exists import ensure_dir_exists


def make(mk):
    lst = get_list_of_all_pdfs('./pdf')
    for file_info in lst:
        file_base = file_info['file_base']
        dir_base  = file_info['dir_base']
        print(file_base)
        cmdstr = mk._render_template(FILE_BASE=file_base, DIR_BASE=dir_base)
        print(mk.make(FILE_BASE=file_base, DIR_BASE=dir_base))
        print('---')
        

def ensure_css():
    dst_dir = '.\\html\\css'
    ensure_dir_exists(dst_dir)
    for src in ['.\\util\\style.css', '.\\util\\index.css']:
        cmd = 'xcopy "{}" "{}" /D /Y'.format(src, dst_dir)
        os.system(cmd)

    
@click.group()
def cli():
    '''Split pdfs in halve (or not, you can choose), translate them to png, and add comments and notes to each png in restructured text format. After translation to html the notes appear next to the pngs.

    There are three phases to the process:
  
    1. Place pdfs in the pdf-directory and split them into halves (optional), then translate the split pdf into pngs and create an initial restructured text file which links to all pngs. This process is automatic and started by running 'make.py build`.

    2. Copy the rst files from the build directory to the main directory. From here the next step is picking up the files. This second step here is manual and deliberately so in order to decouple the automatic translation from pdf to rst and the manual editing of the copied rst files. It is not possible not accidently overwrite the already edited rst files.
    
    3. In the copied rst directory, the rst files can be edit, and pngs can be modified. Run 'make.py html' to translate the rst files to html. The pngs are mklinked to the html directory. In addition an index html file is created.
    '''
    pass
    
@cli.command()
def html():
    '''
    Translate rst to html, mklink to pngs.
    '''
    mk = Make('util/Makefile_html.tpl')
    make(mk)
    make_index()
    ensure_css()
    
@cli.command()
def build():
    '''
    Split pdf, translate to png, create rst.
    
    Manually copy the files to the rst folder to be processed by the html command.
    '''
    mk = Make('util/Makefile_build.tpl')
    make(mk)
    
if __name__ == '__main__':
    cli()


    

