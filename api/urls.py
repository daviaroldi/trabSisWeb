from django.conf.urls import include, url

# from . import views
from rest_framework import routers
from .viewsets.contract import ContractViewSet
from .viewsets.client import ClientViewSet
from .viewsets.document import DocumentViewSet
from .viewsets.proposal import ProposalViewSet

router = routers.DefaultRouter()
router.register(r'contracts', ContractViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'proposal', ProposalViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]