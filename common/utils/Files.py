import os, shutil

class Files():

  @staticmethod
  def emptyDir(directory):
    if os.path.exists(directory):
      shutil.rmtree(directory)
    os.makedirs(directory)

  @staticmethod
  def removeDir(directory):
    if os.path.isdir(directory):
      print 'removing : %s' % directory
      shutil.rmtree(directory)

  @staticmethod
  def removeDirsRecursive(root, filterExpr):
    for root, dirs, files in os.walk(root):
      for dir in filter(filterExpr, dirs):
        dirPath = os.path.join(root, dir)
        print 'removing : %s' % dirPath
        shutil.rmtree(dirPath)

  @staticmethod
  def removeFilesRecursive(root, filterExpr):
    for root, dirs, files in os.walk(root):
      for file in filter(filterExpr, files):
        filePath = os.path.join(root, file)
        print 'removing : %s' % filePath
        os.remove(filePath)