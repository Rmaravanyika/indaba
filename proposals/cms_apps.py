from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ProposalApphook(CMSApp):
    name = _("Proposals")
    urls = ["proposals.urls"]
    app_name = "proposals"
apphook_pool.register(ProposalApphook)
# give your application a name (required)
# link your app to url configuration(s)
