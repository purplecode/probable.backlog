import datetime
from Issue import Issue

class IssueWithSubtasks(Issue):

  def __init__(self, issue, order, collection, subtasksCollection):
    Issue.__init__(self, issue, order, collection)
    self.subtasks =  list(subtasksCollection.find({'parent': self.getKey()}))

  def getSubtasks(self):
    return map(self.__createSubtask, self.subtasks) or []

  def __createSubtask(self, subtask):
    return {key: subtask[key] for key in ('key', 'url', 'status', 'priority', 'issueType', 'summary', 'progress')}

  def getStatus(self):
    statuses = set([subtask['status'] for subtask in self.getSubtasks()])
    if statuses == set(['Closed']) or self.issue.fields.status.name == 'Closed':
      return 'Closed'
    if not statuses or statuses == set(['Open']):
      return 'Open'
    if statuses == set(['Resolved', 'Closed']):
      return 'In Review'
    return 'In Progress'

  def getProgress(self):

      parentProgress = Issue.getProgress(self)
      
      maxIfNotClosed = lambda key: max(parentProgress[key], self.__sumUpProgress(subtasks, key)) if self.getStatus() != 'Closed' else self.__sumUpProgress(subtasks, key)

      subtasks = self.getSubtasks()
      result = {
          "timespent": self.__sumUpProgress(subtasks, 'timespent'),
          "current": self.__sumUpProgress(subtasks, 'current'),
          "total":  maxIfNotClosed('total'),
          "estimate":  maxIfNotClosed('estimate'),
      }

      result['percent'] = round(float(result['timespent']) / result['total'] * 100, 2) if result['total'] > 0 else 0
      return result

  def __sumUpProgress(self, subtasks, property):
      return reduce((lambda acc, subtask: acc + subtask['progress'][property]), subtasks, 0)
