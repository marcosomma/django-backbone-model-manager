from django.db import models


class Course(models.Model): 

    identifier = models.CharField(unique=True, blank=False, max_length=35)
    name = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=True)
    duration = models.IntegerField(blank=False)

    def __unicode__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(blank=False, max_length=100)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.name

class Topic(models.Model):

    name = models.CharField(blank=False, max_length=100)
    identifier = models.CharField(blank=True, max_length=35)
    lesson = models.ForeignKey(Lesson)

    def __unicode__(self):
        return self.name