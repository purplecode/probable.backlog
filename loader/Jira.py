from loader.settings import settings
from loader.Project import Project

class Jira(object):

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def getProject(self, name):
    return Project(settings[name], self.username, self.password)