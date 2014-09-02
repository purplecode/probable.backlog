from loader.model.Issue import Issue

class Epic(Issue):

  def __init__(self, issue, order, storiesCollection):
    Issue.__init__(self, issue, order)
    self.stories = list(storiesCollection.find({'parent': self.getKey()}))

  def getSubtasks(self):
    return map(self.__createSubtask, self.stories)

  def getProgress(self):
    result = {
        "timespent": self.__sumUpProgress('timespent'),
        "current": self.__sumUpProgress('current'),
        "total": self.__sumUpProgress('total'),
        "estimate": self.__sumUpProgress('estimate')
    }
    result['percent'] = float(result['current']) / result['total'] * 100 if result['total'] > 0 else 0;
    return result

  def __sumUpProgress(self, property):
    return reduce((lambda acc, story: acc + story['progress'][property]), self.stories, 0)

  def __createSubtask(self, subtask):
    return {key: subtask[key] for key in ('key', 'url', 'status', 'priority', 'issueType', 'summary', 'progress')}


