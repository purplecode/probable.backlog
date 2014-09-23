from loader.model.Issue import Issue

class Story(Issue):

  def getParentKey(self):
    if hasattr(self.issue.fields, 'customfield_12790') and self.issue.fields.customfield_12790:
      return self.issue.fields.customfield_12790
    return Issue.getParentKey(self)

  def getSubtasks(self):
    map(self.__createSubtask, self.issue.fields.subtasks)

  def __createSubtask(self, subtask):
    fields = subtask.fields
    return {
      "key": subtask.key,
      "url": subtask.self,
      "status": fields.status.name,
      "priority": fields.priority.name,
      "issueType": fields.issuetype.name,
      "summary": fields.summary
    }


