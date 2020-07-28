import sys

from read_docx import process_docx_document
from write_602 import write_to_602
from read_pdf import process_pdf_document
from open_dosbox import open_dosbox

def main():
    #read_file_path = "C:\DOS\SAMPLES\POSUDEK\POSUDEK.docx"
    #read_file_path = "C:\DOS\SAMPLES\Feromony.docx"
    #write_file_path = "Feromony.602"
    input_file_path = sys.argv[1]
    output_file_name = sys.argv[2]

    if input_file_path.split(".")[1] == "docx":
        document_text = process_docx_document(input_file_path)
    elif input_file_path.split(".")[1] == "pdf":
        document_text = process_pdf_document(input_file_path)
    else:
        return

    tab_len_int = 4 #tab lenght
    lm_int = 1 #left margin
    rm_int = 65 #right margin
    pl_int = 55 #page length
    mt_int = 3 #top margin
    mb_int = 3 #bottom margin
    po_int = 5 #print from column
    pn_int = 1 #print from page number

    dos_dir_path = "C:\DOS"
    output_file_path = "{0}\{1}.602".format(dos_dir_path, output_file_name)
    dosbox_path = "C:\Program Files (x86)\DOSBox-0.74-3\DOSBox.exe"

    write_to_602(document_text, output_file_path, tab_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int)
    open_dosbox(dosbox_path, output_file_name)

main()