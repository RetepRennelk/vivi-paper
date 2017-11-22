import re
from subprocess import Popen, PIPE

class Make():
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self._template = f.read()
                
    def _render_template(self, **kwargs):
        cmdstr = self._template
        for key in kwargs:
            pattern = '({{{{\s*{}\s*}}}})'.format(key)
            cmdstr = re.sub(pattern, kwargs[key], cmdstr)
        return cmdstr

    def make(self, **kwargs):
        cmdstr = self._render_template(**kwargs);
        p = Popen(['make','-f','-'], stdin=PIPE, stdout=PIPE)
        p.stdin.write(cmdstr.encode('utf-8'))
        cmdstr = p.communicate()[0]
        p.stdin.close()
        return cmdstr

