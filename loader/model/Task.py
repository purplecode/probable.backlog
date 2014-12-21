from loader.model.Issue import Issue


class Task(Issue):

    def getParentKey(self):
        if hasattr(self.issue.fields, 'parent') and self.issue.fields.parent.key:
            return self.issue.fields.parent.key
        return Issue.getParentKey(self)

    def getStatus(self):
        return self.issue.fields.status.name

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

