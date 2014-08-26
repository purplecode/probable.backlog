import getpass
from common.database.Database import Database
from loader.Jira import Jira
from loader.settings import settings as projects

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


def loadIssues(collection, issues, removeQuery):
  print collection.fullName()
  collection.remove(removeQuery)
  for issue in issues:
    print issue.getKey()
    collection.insert(issue.getModel())


if __name__ == "__main__":
  username = raw_input('login: ')
  password = getpass.getpass('password: ')

  database = Database(database='backlog', port=27017).authenticateWithKeyPass('backlog')

  for projectKey, settings in projects.iteritems():
    project = Jira(username, password).getProject(projectKey)
    loadIssues(database.getCollection('projects'), [project], {'key' : projectKey})
    loadIssues(database.getCollection('epics'), project.getEpics(), {'project_key' : projectKey})
    loadIssues(database.getCollection('stories'), project.getStories(), {'project_key' : projectKey})




