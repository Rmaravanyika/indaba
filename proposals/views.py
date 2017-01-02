from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView,)

from proposals.models import   Proposal, Talk_Type
from proposals.forms import ProposalForm


class CreateProposal(CreateView):
    model = Proposal
    form_class = ProposalForm
    template_name = "proposals/talk_form.html"

    def get_form_kwargs(self):
        kwargs = super(CreateProposal, self).get_form_kwargs()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateProposal, self).get_context_data(**kwargs)
        return context
