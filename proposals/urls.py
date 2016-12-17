from django.conf.urls import  url, include
# from rest_framework import routers

from proposals.views import (CreateProposal)

# router = routers.DefaultRouter()
# router.register(r'talks', TalksViewSet)

urlpatterns = [ 
    url(r'^submit_talk', CreateProposal.as_view(), name='create_talks'),
]
