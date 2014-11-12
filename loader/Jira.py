from jira.client import JIRA
from loader.model.Project import Project
from loader.settings import settings
from loader.model.Task import Task
from loader.model.Story import Story
from loader.model.Epic import Epic

class Jira(object):

  def __init__(self, projectKey, username, password):
    self.queries = settings[projectKey]['queries']
    self.jira = JIRA(options={'server': settings[projectKey]['url']}, basic_auth=(username, password))

  def getProject(self):
    return Project(self.jira.project(self.queries['project']))

  def getTasks(self, tasks):
    return [Task(issue, idx, tasks) for idx, issue in enumerate(self.jira.search_issues(self.queries['tasks']))]

  def getStories(self, stories):
    epicIds = map(lambda epic: epic.key, self.jira.search_issues(self.queries['epics']))
    storiesQuery = self.queries['stories'] % ",".join(epicIds)
    print storiesQuery
    return [Story(issue, idx, stories) for idx, issue in enumerate(self.jira.search_issues(storiesQuery))]

  def getEpics(self, epics, stories):
    return [Epic(issue, idx, epics, stories) for idx, issue in enumerate(self.jira.search_issues(self.queries['epics']))]
