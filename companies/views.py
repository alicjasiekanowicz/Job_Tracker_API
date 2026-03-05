from rest_framework.viewsets import ModelViewSet
from .models import Company
from .serializers import CompanySerializer

# Create your views here.
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)