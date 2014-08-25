from jira.client import JIRA
from loader.Issue import Issue


class Project(object):
  def __init__(self, configuration, username, password):
    self.queries = configuration['queries']
    self.__connect(configuration, username, password)
    self.project = self.jira.project(self.queries['project'])

  def __connect(self, configuration, username, password):
    options = {
      'server': configuration['url']
    }
    self.jira = JIRA(options=options, basic_auth=(username, password))

  def getKey(self):
    return self.project.key

  def getStories(self):
    return self.__getIssues('stories')

  def getEpics(self):
    return self.__getIssues('epics')

  def __getIssues(self, name):
    return [Issue(issue, idx) for idx, issue in enumerate(self.jira.search_issues(self.queries[name]))]

  def getModel(self):
    return {
      "id": self.project.key,
      "name": self.project.name,
      "description": self.project.description,
      "lead": {
        "displayName": self.project.lead.displayName,
        "username": self.project.lead.name,
        "avatar": getattr(self.project.lead.avatarUrls, '48x48')
      },
      "versions": map(lambda version: version.name, self.project.versions),
      "url": self.project.self,
      "application": self.project.url
    }
