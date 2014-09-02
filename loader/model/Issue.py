class Issue(object):
  def __init__(self, issue, order):
    self.issue = issue
    self.order = order

  def getKey(self):
    return self.issue.key

  def getParentKey(self):
    return 'undefined'

  def getSubtasks(self):
    return []

  def getProgress(self):
    toHours = lambda obj, key, unit=3600.0: float(getattr(obj, key))/unit if hasattr(obj, key) and getattr(obj, key) else 0.0
    fields = self.issue.fields
    return {
        "timespent": toHours(fields, 'aggregatetimespent'),
        "current": toHours(fields.aggregateprogress, 'progress'),
        "total": toHours(fields.aggregateprogress, 'total'),
        "percent": toHours(fields.aggregateprogress, 'percent', 1),
        "estimate" : max(toHours(fields, 'customfield_11890'), toHours(fields, 'aggregatetimeoriginalestimate'))
    }

  def getModel(self):
    issue = self.issue
    fields = self.issue.fields
    model = {
      "key": issue.key,
      "order": self.order,
      "url": issue.self,
      "priority": fields.priority.name,
      "status": fields.status.name,
      "issueType": fields.issuetype.name,
      "summary": fields.summary,
      "project_name": fields.project.name,
      "project_key": fields.project.key,
      "last_update": fields.updated,
      "labels": fields.labels,
      "versions": map(lambda version: version.name, fields.versions),
      "dueDate": fields.duedate,
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
