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
    return [Story(issue, idx, stories) for idx, issue in enumerate(self.jira.search_issues(self.queries['stories']))]

  def getEpics(self, epics, stories):
    return [Epic(issue, idx, epics, stories) for idx, issue in enumerate(self.jira.search_issues(self.queries['epics']))]
