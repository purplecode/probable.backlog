import datetime, abc

class Issue(object):

    def __init__(self, issue, order, collection):
        self.issue = issue
        self.order = order
        self.previous = collection.findOne({'key': self.getKey()}) or {}

    @abc.abstractmethod
    def getParentKey(self):
        pass

    @abc.abstractmethod
    def getSubtasks(self):
        pass

    @abc.abstractmethod
    def getStatus(self):
        pass

    def getProgress(self):
        fields = self.issue.fields
        getPoints = lambda obj, key: float(getattr(obj, key)) if hasattr(obj, key) and getattr(obj, key) else 0.0
        estimate = max(getPoints(fields, 'customfield_11890'), getPoints(fields, 'aggregatetimeoriginalestimate'), getPoints(fields.aggregateprogress, 'total'), 0.0)
        if estimate > 100:
            estimate /= 3600
        timespent = self.__timespent(estimate)
        return {
            "timespent": timespent,
            "current": timespent,
            "total": estimate,
            "percent": round(timespent / estimate, 2) if estimate > 0 else 0,
            "estimate": estimate
        }

    def __timespent(self, points):
        status = self.getStatus()
        if status == "In Review":
            return points / 2
        if status == "Open":
            return 0
        return points

    def getKey(self):
        return self.issue.key

    def getHistory(self):
        history = self.previous.get('history') or []
        progress = self.getProgress()
        progress['datetime'] = datetime.datetime.now().isoformat()
        if progress['total'] > 0:
            history += [progress]
        return history

    def getModel(self):
        issue = self.issue
        fields = self.issue.fields
        model = {
            "key": issue.key,
            "order": self.order,
            "url": issue.self,
            "priority": fields.priority.name,
            "status": self.getStatus(),
            "issueType": fields.issuetype.name,
            "summary": fields.summary,
            "project_name": fields.project.name,
            "project_key": fields.project.key,
            "last_update": fields.updated,
            "labels": fields.labels,
            "versions": map(lambda version: version.name, fields.versions),
            "dueDate": fields.duedate or "",
            "creationDate": fields.created,
            "resolutionDate": fields.resolutiondate,
            "fixVersions": map(lambda version: version.name, fields.fixVersions),
            "components": map(lambda component: component.name, fields.components),
            "description": fields.description,
            "votes": fields.votes.votes,
            "environment": fields.environment,
            "estimate": fields.aggregatetimeestimate,
            "originalEstimate": fields.aggregatetimeoriginalestimate,
            "progress": self.getProgress(),
            "history": self.getHistory(),
            "subtasks": self.getSubtasks(),
            "parent": self.getParentKey()
        }

        if fields.assignee:
            model['assignee'] = {
                "displayName": fields.assignee.displayName,
                "username": fields.assignee.name,
                "email": fields.assignee.emailAddress,
                "avatar": getattr(fields.assignee.avatarUrls, '48x48')
            }

        if fields.reporter:
            model['reporter'] = {
                "displayName": fields.reporter.displayName,
                "username": fields.reporter.name,
                "email": fields.reporter.emailAddress,
                "avatar": getattr(fields.reporter.avatarUrls, '48x48')
            }

        return model
