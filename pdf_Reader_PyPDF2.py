import PyPDF2

'''
object = open("K:/Users/David's/Desktop/MyProj/DATA/STAAR.pdf","rb")

input = PyPDF2.PdfFileReader(object)

if input.isEncrypted:
    input.decrypt()


page = input.getPage(2)


output = page.extractText()

print(output)

'''
# creating a pdf file object

pdfFileObj = open("K:/Users/David's/Desktop/MyProj/DATA/STAAR.pdf", "rb")

# creating a pdf reader object

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file

print(pdfReader.numPages)

# creating a page object

pageObj = pdfReader.getPage(10)

# extracting text from page

print(pageObj.extractText())

# Closing the pdf file object

pdfFileObj.close()

