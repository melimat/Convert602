import sys

from read_docx import process_docx_document
from read_pdf import process_pdf_document
from write_602 import write_to_602
from open_dosbox import open_dosbox

def convert(input_file_path, output_file_name, dos_dir_path, dosbox_path, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int):

    if input_file_path.split(".")[1] == "docx":
        document_text = process_docx_document(input_file_path)
    elif input_file_path.split(".")[1] == "pdf":
        document_text = process_pdf_document(input_file_path)
    else:
        return

    output_file_path = "{0}\{1}.602".format(dos_dir_path, output_file_name)

    write_to_602(document_text, output_file_path, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int)
    open_dosbox(dosbox_path, output_file_name)