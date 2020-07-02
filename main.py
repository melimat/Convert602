import sys

from read_docx import process_docx_document
from write_602 import write_to_602
from read_pdf import process_pdf_document

def main():
    #read_file_path = "C:\DOS\SAMPLES\POSUDEK\POSUDEK.docx"
    #read_file_path = "C:\DOS\SAMPLES\Feromony.docx"
    #write_file_path = "Feromony.602"
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    if input_file_path.split(".")[1] == "docx":
        document_text = process_docx_document(input_file_path)
    elif input_file_path.split(".")[1] == "pdf":
        document_text = process_pdf_document(input_file_path)
    else:
        return

    write_to_602(document_text, output_file_path)

main()