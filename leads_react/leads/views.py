from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics

#the use of generic views to get and post requests
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer