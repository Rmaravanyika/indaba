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
    
class Proposal(models.Model):

    abstract = MarkupField()
    title = models.CharField(max_length=255)
    talk_type = models.ForeignKey(Talk_Type)

