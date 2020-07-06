import sys
import os
from .serializers import ArquivosSerializer
from .models import Arquivos
from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .methods.merge import merge
from .methods.getInformations import getInformations
from .methods.slipt import IntervalSplit



class JuntarPDF(APIView):

    # def get(self, request, format=None):
    #     fs = FileSystemStorage()
    #     filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'VPN Patriarca.pdf')
    #     if fs.exists(filename):
    #         with fs.open(filename) as pdf:
    #             response = HttpResponse(pdf, content_type='application/pdf')
    #             response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    #             return response
        

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



class DividirPDF(APIView):

    def post(self, request, format=None):
        arquivo = request.data.get('arquivo0')
        if request.data.get('getInformation') == 'true':
            data = getInformations(arquivo)
            return JsonResponse(data)
        else:
            # ajustar as páginas que são selecionadas
            start = int(request.data.get('start'))
            end = int(request.data.get('end'))
            IntervalSplit(arquivo, start, end)

            fs = FileSystemStorage()
            # Buscando o arquivo que foi criado
            filename = os.path.join(os.path.dirname(os.path.abspath(__package__)), 'document-output.pdf')
            if fs.exists(filename):
                with fs.open(filename) as pdf:
                    response = HttpResponse(pdf, content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
                    return response
       

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