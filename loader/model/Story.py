from loader.model.IssueWithSubtasks import IssueWithSubtasks

class Story(IssueWithSubtasks):

  def getParentKey(self):
    if hasattr(self.issue.fields, 'customfield_12790') and self.issue.fields.customfield_12790:
      return self.issue.fields.customfield_12790
    return Issue.getParentKey(self)
