import os

class KeyPass(object):

  POSTGRES = '~/.pgpass'
  MONGO = '~/.mongopass'
  MYSQL = '~/.mysqlpass'

  def getDatabasePassword(self, passfile, host='*', port='*', database="*", username='*'):
    return self.getPassword(passfile, host, port, database, username)

  def getPassword(self, passfile, *args):
    with open(os.path.expanduser(passfile)) as passfile:
      for entry in passfile:
          entry = entry.strip().split(':')
          if self._matches(entry[0:len(args)], map(str, args)):
              return entry[-1]

  def _matches(self, entryPrefix, args):
    assert len(entryPrefix) == len(args)
    return all([(property == '*' or arg  == '*' or property == arg) for property, arg in zip(entryPrefix, args)])
