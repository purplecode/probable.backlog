import argparse, getpass
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
  parser = argparse.ArgumentParser()

  parser.add_argument('-u', '--username', dest='username', default="mjaworsk", help='username')
  parser.add_argument('-p', '--password', dest='password', help='password')
 
  args = parser.parse_args()

  if not args.password:
    password = getpass.getpass('password: ')
  else:
    password = args.password

  database = Database(database='backlog', port=27017).authenticateWithKeyPass('backlog')

  for projectKey, settings in projects.iteritems():
    projects = database.getCollection('projects')
    tasks = database.getCollection('tasks')
    stories = database.getCollection('stories')
    epics = database.getCollection('epics')

    jira = Jira(projectKey, args.username, password)
    loadIssues(projects, [jira.getProject()], {'key' : projectKey})
    loadIssues(tasks, jira.getTasks(tasks), {'project_key' : projectKey})
    loadIssues(stories, jira.getStories(stories), {'project_key' : projectKey})
    loadIssues(epics, jira.getEpics(epics, stories), {'project_key' : projectKey})




