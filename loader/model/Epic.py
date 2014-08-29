from loader.model.Issue import Issue

class Epic(Issue):

  def __init__(self, issue, order, storiesCollection):
    Issue.__init__(self, issue, order)
    self.stories = list(storiesCollection.find({'parent': self.getKey()}))

  def getSubtasks(self):
    return map(self.__createSubtask, self.stories)

  def getProgress(self):
    return {
        "timespent": self.__sumUpProgress('timespent'),
        "current": self.__sumUpProgress('current'),
        "total": self.__sumUpProgress('total'),
        "percent": self.__sumUpProgress('percent')
    }

  def __sumUpProgress(self, property):
    result = reduce((lambda acc, story: acc + story['progress'][property]), self.stories, 0),
    return result[0] # wtf?

  def __createSubtask(self, subtask):
    return {key: subtask[key] for key in ('key', 'url', 'status', 'priority', 'issueType', 'summary')}


