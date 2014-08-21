import getpass, json
from loader.Jira import Jira
from database.Database import Database


def isAnyInstance(obj, *types):
  return any(map(lambda type: isinstance(obj, type), types))


def objToDict(obj):
  if hasattr(obj, "__iter__"):
    return map(lambda item: objToDict(item), obj)
  elif hasattr(obj, "__dict__"):
    current = {}
    for field, value in obj.__dict__.iteritems():
      if not field.startswith('custom') and not field.startswith('_'):
        current[field] = objToDict(value)
    return current
  else:
    return obj


def loadIssues(collection, issues):
  for issue in issues:
    print issue.getKey()
    collection.update({'key': issue.getKey()}, issue.getModel(), upsert=True)


if __name__ == "__main__":
  username = raw_input('login: ')
  password = getpass.getpass('password: ')

  database = Database(database='backlog', port=27017).authenticateWithKeyPass('backlog')
  project = Jira(username, password).getProject('MINT')

  loadIssues(database.getCollection('stories'), project.getStories())
  loadIssues(database.getCollection('epics'), project.getEpics())
  loadIssues(database.getCollection('projects'), [project])




