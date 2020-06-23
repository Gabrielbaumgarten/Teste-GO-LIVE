from .serializers import ArquivosSerializer
from .models import Arquivos
from rest_framework import generics

class JuntarPDF(generics.ListCreateAPIView):
    queryset = Arquivos.objects.all()
    serializer_class = ArquivosSerializer

class DividirPDF(generics.ListCreateAPIView):
    queryset = Arquivos.objects.all()
    serializer_class = ArquivosSerializer

class ComprimirPDF(generics.ListCreateAPIView):
    queryset = Arquivos.objects.all()
    serializer_class = ArquivosSerializer

class PDFtoJPG(generics.ListCreateAPIView):
    queryset = Arquivos.objects.all()
    serializer_class = ArquivosSerializer

class PesquisarPDF(generics.ListCreateAPIView):
    queryset = Arquivos.objects.all()
    serializer_class = ArquivosSerializer

