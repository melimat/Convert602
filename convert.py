import sys

from read_docx import process_docx_document
from read_pdf import process_pdf_document
from write_602 import write_to_602
from open_dosbox import open_dosbox

def convert(open_dosbox_bool, input_file_path, output_file_path, dos_dir_path, dosbox_path, tab_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int):
    file_type = determine_file_type(input_file_path)
    if file_type == "docx":
        document_text = process_docx_document(input_file_path)
    elif file_type == "pdf":
        document_text = process_pdf_document(input_file_path)
    else:
        return

    write_to_602(document_text, output_file_path, tab_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int)
    
    if open_dosbox_bool == True:
        open_dosbox(dosbox_path, output_file_path, dos_dir_path)

def determine_file_type(path):
    dot_splitted_list = path.split(".")
    return dot_splitted_list[len(dot_splitted_list) - 1]