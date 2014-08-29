
class Project(object):

  def __init__(self, project):
    self.project = project

  def getKey(self):
    return self.project.key

  def getModel(self):
    return {
      "id": self.project.key,
      "key": self.project.key,
      "name": self.project.name,
      "description": self.project.description,
      "lead": {
        "displayName": self.project.lead.displayName,
        "username": self.project.lead.name,
        "avatar": getattr(self.project.lead.avatarUrls, '48x48')
      },
      "versions": map(lambda version: version.name, self.project.versions),
      "url": self.project.self,
      "application": self.project.url if hasattr(self.project, 'url') else '',
    }
