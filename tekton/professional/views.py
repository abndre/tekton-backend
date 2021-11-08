from rest_framework import generics
from .models import Professional
from .serializers import ProfessionalSerializer


# Create your views here.
class ProfessionalList(generics.ListCreateAPIView):

    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
