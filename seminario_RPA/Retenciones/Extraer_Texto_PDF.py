from tkinter import N
import PyPDF2
import sys
import pyperclip

path = sys.argv[1]
file = sys.argv[2]
pdfPath = path+file

pdfPath=pdfPath.replace("¤"," ")

pdfFileObject = open(pdfPath, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages
aux=''

for i in range(count):
    page = pdfReader.getPage(i)
    output = page.extractText()
    aux=aux+"\n"
    aux=aux+output

pyperclip.copy(aux)
print(aux)