from rest_framework.viewsets import ModelViewSet
from .models import Company
from .serializers import CompanySerializer

# Create your views here.
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        print("user",self.request.user)
        return Company.objects.filter(created_by= self.request.user)
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(created_by =self.request.user)

    