
# Import relevent pdf miner dependencies
import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice 

from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal

# Get PDF File to parse 
screenplay = open('Documents/Reggie.pdf','rb')

# Create a PDF parser object
parser = PDFParser(screenplay)

# Create the pdf document object
document = PDFDocument(parser)

# Check if the document allows extraction. If not, abort.
if not doucment.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources
# In this case, shared resources shouldn't be relevant, but let's set it up just in case
resourcemanager = PDFResourceManager()

# Set parameters for analysis.
laparams = LAParams()

# Create a PDF Device
# I think devices are what turn my code into other stuff? Idk, but I want this to export a json file
device = PDFPageAggregator(resourcemanager, laparams=laparams)

# Create a PDF Interpreter 
# I think the Interpreter is what actually processes the pdf
# from it's raw code to something more akin to what we read.
interpreter = PDFPageInterpreter(resourcemanager,device)


# Process each page contained in the document
# This is a loop that checks each page in the script supplied
for page in PDFPage.create_pages(document) :
    interpreter.process_page(page)

    layout = device.get_result()
    for element in layout:
        if isinstance(element,LTTextBoxHorizontal):
            print(element.get_text())