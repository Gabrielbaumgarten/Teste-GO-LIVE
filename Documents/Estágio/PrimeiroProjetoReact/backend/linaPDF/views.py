from .serializers import ArquivosSerializer
from .models import Arquivos
from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse
import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from .merge import merge
import sys
# class JuntarPDF(generics.ListCreateAPIView):
#     queryset = Arquivos.objects.all()
#     serializer_class = ArquivosSerializer


class JuntarPDF(APIView):

    def get(self, request, format=None):
        fs = FileSystemStorage()
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'VPN Patriarca.pdf')
        if fs.exists(filename):
            with fs.open(filename) as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
                return response
        

    def post(self, request, format=None):
        arquivos = []
        for index in range(len(request.data)):
            aux = 'arquivo' + str(index)
            arquivos.append(request.data.get(aux)) 
        output = merge(arquivos)
        
        fs = FileSystemStorage()
        # Buscando o arquivo que foi criado
        filename = os.path.join(os.path.dirname(os.path.abspath(__package__)), 'document-output.pdf')
        if fs.exists(filename):
            with fs.open(filename) as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
                return response



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

class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                      cls, *args, **kwargs)
        return cls._instance