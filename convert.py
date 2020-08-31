import sys

from read_docx import process_docx_document
from Pdf_processor import Pdf_processor
from write_602 import write_to_602
from open_dosbox import open_dosbox

def convert(open_dosbox_bool, chars_limit, input_file_path, output_file_path, dos_dir_path, dosbox_path, tab_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int):
    file_type = determine_file_type(input_file_path)
    if file_type == "docx":
        document_text = process_docx_document(input_file_path)
        write_to_602(document_text, output_file_path, tab_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int)
        if open_dosbox_bool == True:
            open_dosbox(dosbox_path, output_file_path, dos_dir_path)
        
        return


    elif file_type == "pdf":
        pdf_processor = Pdf_processor(input_file_path, chars_limit)
        pdf_processor.process_pdf_document()
        if pdf_processor.is_text_segmented:
            filepath_splitted = output_file_path.split(".602")
            filepath_without_suffix = filepath_splitted[0]

            filepath_list = []

            for index, eachelement in enumerate(pdf_processor.text_segments_list):
                filepath = filepath_without_suffix + "{0}.602".format(index + 1)
                filepath_list.append(filepath)
                write_to_602(eachelement, filepath, tab_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int)
            
            if open_dosbox_bool == True:
                open_dosbox(dosbox_path, filepath_list[0], dos_dir_path)
            
            return
        
        else:
            document_text = pdf_processor.whole_text
            write_to_602(document_text, output_file_path, tab_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int)

            if open_dosbox_bool == True:
                open_dosbox(dosbox_path, output_file_path, dos_dir_path)
            
            return
    else:
        return
    
    

def determine_file_type(path):
    dot_splitted_list = path.split(".")
    return dot_splitted_list[len(dot_splitted_list) - 1]