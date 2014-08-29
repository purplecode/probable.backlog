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

  def getTasks(self):
    return [Task(issue, idx) for idx, issue in enumerate(self.jira.search_issues(self.queries['tasks']))]

  def getStories(self):
    return [Story(issue, idx) for idx, issue in enumerate(self.jira.search_issues(self.queries['stories']))]

  def getEpics(self, storiesCollection):
    return [Epic(issue, idx, storiesCollection) for idx, issue in enumerate(self.jira.search_issues(self.queries['epics']))]
