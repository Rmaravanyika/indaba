from django.contrib import admin
from proposals.models import Proposal, Talk_Type
from django import forms


class TalkAdmin(admin.ModelAdmin):
    list_dispaly = ("title", "talk_type",)
    list_editable = ('status')

    # form = AdminTalkForm

admin.site.register(Proposal)
admin.site.register(Talk_Type)
