import copy

from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.module_loading import import_string
from django.utils.translation import ugettext as _

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from markitup.widgets import MarkItUpWidget
from easy_select2.widgets import Select2Multiple

from wafer.talks.models import Talk, render_author


def get_proposal_form_class():
    pass

class ProposalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        initial = kwargs.setdefault('initial', {})

        super(ProposalForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        submit_button = Submit('submit', _('Submit'))
        instance = kwargs['instance']
        if instance:
            self.helper.layout.append(
                FormActions(
                    submit_button,
                    HTML('<a href="%s" class="btn btn-danger">%s</a>'
                         % (reverse('wafer_talk_delete', args=(instance.pk,)),
                            _('Delete')))))
        else:
            self.helper.add_input(submit_button)

    class Meta:
        model = Proposal
        fields = ('title', 'talk_type', 'abstract')
        widgets = {
            'abstract': MarkItUpWidget(),
            'notes': forms.Textarea(attrs={'class': 'input-xxlarge'}),
            'authors': Select2Multiple(),
        }
