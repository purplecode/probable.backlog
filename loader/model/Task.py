from loader.model.Issue import Issue

class Task(Issue):

  def getParentKey(self):
    if hasattr(self.issue.fields, 'parent') and self.issue.fields.parent.key:
      return self.issue.fields.parent.key
    return Issue.getParentKey(self)
