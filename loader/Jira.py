from jira.client import JIRA
from loader.model.Project import Project
from loader.settings import settings
from loader.model.Task import Task
from loader.model.Story import Story
from loader.model.Epic import Epic


class Jira(object):
    def __init__(self, projectKey, username, password):
        self.queries = settings[projectKey]['queries']
        self.jira = JIRA(options={'server': settings[projectKey]['url']}, basic_auth=(username, password))

        keys = lambda issues: map(lambda issue: issue.key, issues)

        self.epics = self.__searchIssues(self.queries['epics'])
        self.stories = self.__searchIssuesByParents(self.queries['stories'], keys(self.epics))
        self.tasks = self.__searchIssuesByParents(self.queries['tasks'], keys(self.stories))

    def getProject(self):
        return Project(self.jira.project(self.queries['project']))

    def getTasks(self, tasks):
        return [Task(issue, idx, tasks) for idx, issue in enumerate(self.tasks)]

    def getStories(self, stories, tasks):
        return [Story(issue, idx, stories, tasks) for idx, issue in enumerate(self.stories)]

    def getEpics(self, epics, stories):
        return [Epic(issue, idx, epics, stories) for idx, issue in enumerate(self.epics)]

    def __searchIssues(self, query):
        print query
        return self.jira.search_issues(query, maxResults=1000)

    def __searchIssuesByParents(self, queryTmpl, parentIds):
        pageSize = 10
        result = []
        for init in xrange(len(parentIds) / pageSize + 1):
            ids = parentIds[init * pageSize:init * pageSize + pageSize]
            if ids:
              query = queryTmpl % ",".join(ids)
              result += self.__searchIssues(query)
        return result
