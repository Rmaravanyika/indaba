from django.db import models
from markitup.fields import MarkupField

ACCEPTED = 'A'
PENDING = 'P'
REJECTED = 'R'


class Talk_Type(models.Model):

    talk_types = (
        ('S', "Short_Talk"),
        ('L', "Long_Talk"),
        ('T', "Tutorial"),
    )

    name = models.CharField(choices=talk_types, max_length=1)

    def __str__(self):
        return u'%s' % (self.name,)


class Proposal(models.Model):

    abstract = MarkupField(help_text="Describe your talk in one or two"
                           "paragraphs, mentioning your target audience & what"
                           "they will get out of your talk"
                           "You are free to use markdown syntax")
    title = models.CharField(max_length=1024)
    talk_type = models.ForeignKey(Talk_Type)

    def __str__(self):
        return self.title


class TalkUrl(models.Model):
    """An url to stuff relevant to the talk - videos, slides, etc.

       Note that these are explicitly not intended to be exposed to the
       user, but exist for use by the conference organisers."""

    description = models.CharField(max_length=256)
    url = models.URLField()
    proposal = models.ForeignKey(Proposal)


class Author(models.Model):
    """ a class to represent the submitter of a talk proposal"""
    name = models.CharField(max_length=255, blank=True)
    talk = models.ForeignKey(Proposal)
