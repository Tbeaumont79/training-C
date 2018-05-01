import sys, pprint
from pysideuic import compileUi
pyfile = open("ui.py", 'w')
compileUi("fenettreprincipal.ui", pyfile, False, 4,
False)
pyfile.close()
