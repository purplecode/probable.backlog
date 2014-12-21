from loader.model.Issue import Issue
from loader.model.IssueWithSubtasks import IssueWithSubtasks

class Epic(IssueWithSubtasks):

  def getParentKey(self):
    return 'N/A'
