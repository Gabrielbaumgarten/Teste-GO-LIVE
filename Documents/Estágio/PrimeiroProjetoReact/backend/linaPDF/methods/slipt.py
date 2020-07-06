import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.core.files.storage import FileSystemStorage


def IntervalSplit(arquivo, inicio, fim):

    output = PdfFileWriter()
    input = PdfFileReader(arquivo)

    for index in range(inicio, fim):
        output.addPage(input.getPage(index))


    fs = FileSystemStorage()
    filename = os.path.join(os.path.dirname(os.path.abspath(__package__)), 'document-output.pdf')
    if fs.exists(filename):
        os.remove(filename)
    outputStream = open("document-output.pdf", "wb")
    output.write(outputStream)
    return outputStream