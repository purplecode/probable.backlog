from loader.model.Issue import Issue

class Epic(Issue):

  def __init__(self, issue, order, stories):
    self.issue = issue
    self.order = order
    self.stories = stories

  def getSubtasks(self):
    subtasks = self.stories.find({'parent': self.getKey()})
    return map(self.__subtask, subtasks)

  def __subtask(self, subtask):
    return {key: subtask[key] for key in ('key', 'url', 'status', 'priority', 'issueType', 'summary')}


