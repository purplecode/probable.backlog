from loader.Project import Project
from loader.settings import settings


class Jira(object):

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def getProject(self, name):
    return Project(settings[name], self.username, self.password)