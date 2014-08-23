from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()
    project_query = models.TextField()
    stories_query = models.TextField()
    epics_query = models.TextField()

    def __unicode__(self):
      return self.name