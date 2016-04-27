from distutils.core import setup
import py2exe

setup(windows=['repast.py'], options={'py2exe':  {'includes':['sip']}})