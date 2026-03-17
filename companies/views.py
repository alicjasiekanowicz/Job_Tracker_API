from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Company
from .serializers import CompanySerializer

# Create your views here.
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'location', 'number_of_workers']
    search_fields = ['name', 'location', 'description', 'website']
    ordering_fields = ['name', 'number_of_workers', 'created_at']
    ordering = ['name']

    def get_queryset(self):
        print("user",self.request.user)
        
        return Company.objects.filter(created_by= self.request.user)
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(created_by =self.request.user)

    