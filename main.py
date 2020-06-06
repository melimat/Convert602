from read_docx import process_docx_document
from write_602 import write_to_602

def main():
    #read_file_path = "C:\DOS\SAMPLES\POSUDEK\POSUDEK.docx"
    read_file_path = "Titrace.docx"
    document_text = process_docx_document(read_file_path)
    write_file_path = "zkouska.602"
    write_to_602(document_text, write_file_path)

main()