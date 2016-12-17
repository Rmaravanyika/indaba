from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView,)

from proposals.models import   Proposal, Talk_Type


class CreateProposal(CreateView):
    model = Proposal
    template_name = "proposals/talk_form.html"
    fields = ['title', 'abstract']

    # def get_form_class(self):
    #     return get_proposal_form_class()

    def get_form_kwargs(self):
        kwargs = super(CreateProposal, self).get_form_kwargs()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateProposal, self).get_context_data(**kwargs)
        return context
