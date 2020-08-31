from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

class Pdf_processor:
    def __init__(self, path_to_pdf_file, chars_limit):
        self.path_to_pdf_file = path_to_pdf_file
        self.is_text_segmented = bool(False)
        self.text_segments_list = []
        self.whole_text = str()
        self.segment_length_limit = chars_limit

    def process_pdf_document(self):

        with open(self.path_to_pdf_file, "rb") as pdf_file:
            output_string = StringIO()
            parser = PDFParser(pdf_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            seg_len = int()
            seg_text = str()
            whole_text = str()

            for index, page in enumerate(PDFPage.create_pages(doc)):
                interpreter.process_page(page)

                page_str = output_string.getvalue()

                print(str(index))

                whole_text += page_str

                output_string.truncate(0)
                output_string.seek(0)

                page_len = len(page_str)
                seg_len += page_len

                if seg_len > self.segment_length_limit:
                    self.text_segments_list.append(seg_text)
                    self.is_text_segmented = True
                    seg_text = str()
                    seg_text += page_str
                    seg_len = page_len
                
                else:
                    seg_text += page_str
            
            self.text_segments_list.append(seg_text)
        
            self.whole_text = whole_text
