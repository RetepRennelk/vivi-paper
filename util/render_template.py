import re

def render_template(filename, **kwargs):
    with open(filename, 'r') as f:
        txt = f.read()
        for key in kwargs:
            pattern = '({{{{\s*{}\s*}}}})'.format(key)
            txt = re.sub(pattern, kwargs[key], txt)
        return txt
        
#print(render_template('Makefile.tpl', text='Rumpel', text2='Rumpelpumpel'))