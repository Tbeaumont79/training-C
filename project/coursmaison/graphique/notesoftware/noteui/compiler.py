import sys, pprint
from pysideuic import compileUi
pyfile = open("main.py", 'w')
compileUi("fenetrePrincipale.ui", pyfile, False, 4,
False)
pyfile.close()
