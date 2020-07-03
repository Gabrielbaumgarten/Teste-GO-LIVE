from PyPDF2 import PdfFileMerger

def merge(arquivos):

    merger = PdfFileMerger()
    
    for index in range(len(arquivos)-1):
        merger.append(fileobj=arquivos[index])
        
    merger.merge(position= index+1, fileobj=arquivos[index+1])

    # Write to an output PDF document
    output = open("document-output.pdf", "wb")
    merger.write(output)
    output.close()
    merger.close()
    return output