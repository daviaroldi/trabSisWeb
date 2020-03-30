from django.conf.urls import include, url

# from . import views
from rest_framework import routers
from .viewsets.ContractViewSet import ContractViewSet
from .viewsets.ClientViewSet import ClientViewSet
from .viewsets.DocumentViewSet import DocumentViewSet
from .viewsets.ProposalViewSet import ProposalViewSet

router = routers.DefaultRouter()
router.register(r'contracts', ContractViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'proposal', ProposalViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]