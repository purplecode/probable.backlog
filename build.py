#!/usr/bin/env python

import os, sys, subprocess
from common.utils.Files import Files

class Config:
  root = '.'
  sources = ['backlog', 'loader', 'common']

########################################################
def test():
  return subprocess.call("py.test", shell=True)

def clean():
  for sourceDir in Config.sources:
    Files.removeDirsRecursive(sourceDir, (lambda d: d == '__pycache__'))
    Files.removeFilesRecursive(sourceDir, (lambda f: f.endswith('.pyc')))

def package():
  for sourceDir in Config.sources:
    for root, dirs, files in os.walk(sourceDir):
      for dir in dirs:
        initFile = os.path.join(root, dir, '__init__.py')
        if not os.path.isfile(initFile):
          print 'creating : %s' % initFile
          open(initFile, 'a').close()

def default():
  clean()
  package()
  test()

########################################################
def step(msg):
  span = '=' * ((80 - len(msg))/2)
  print ' '.join([span, msg, span])

if __name__ == "__main__":
  if len(sys.argv) > 1:
    for task in sys.argv[1:]:
      if task in locals():
        step(task)
        locals()[task]()
      else:
        print 'Error: task "%s" not found' % task
        sys.exit(1)
  else:
    default()
      
 



