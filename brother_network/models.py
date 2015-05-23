"""
Models for the brother network.
"""
from django.contrib.auth.models import User
from django.db import models


"""
Brother Models
"""
class Chapter(models.Model):

    id = models.CharField(max_length=2, primary_key=True, unique=True)
    name = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        self.id = ''
        for i in self.name.upper().split():
            self.id += i[0]
        super(Chapter, self).save(*args, **kwargs)

    def __str__(self):
        return '%s (%s)' % (self.id, self.name)


class Brother(models.Model):

    user = models.OneToOneField(User, primary_key=True)
    chapter = models.ForeignKey(Chapter, default='DB')
    slug = models.SlugField(unique=True)
    groups = models.ManyToManyField('Group', blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.user.username
        super(Brother, self).save(*args, **kwargs)

    def __str__(self):
        return "%s, %s. %s (%s)" % (
            self.user.first_name, self.user.last_name, self.user.username, str(self.chapter.id))


"""
Group Models
"""
class Post(models.Model):

    submitter = models.ForeignKey(Brother)
    content = models.CharField(max_length=1000)
    submit_date = models.DateTimeField()

    def __str__(self):
        return '(%s) %s' % (self.submitter.user.username, self.content)


class Event(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Group(models.Model):

    admin = models.OneToOneField(Brother)
    brothers = models.ManyToManyField(Brother, related_name="Brothers")
    private = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    chapter = models.ForeignKey(Chapter)
    posts = models.ManyToManyField(Post, blank=True)
    events = models.ManyToManyField(Event, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.admin.user.username)