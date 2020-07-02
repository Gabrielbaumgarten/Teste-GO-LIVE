from PyPDF2 import PdfFileMerger

def merge(arquivo1, arquivo2):

    merger = PdfFileMerger()
    
    # add the first 3 pages of input1 document to output
    merger.append(fileobj = arquivo1, pages = (0,1))

    # insert the first page of input2 into the output beginning after the second page
    merger.merge(position = 2, fileobj = arquivo2, pages = (0,1))


    # Write to an output PDF document
    output = open("document-output.pdf", "wb")
    merger.write(output)
    output.close()
    merger.close()
    return output