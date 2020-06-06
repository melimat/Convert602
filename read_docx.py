import docx

read_file_path = "C:\DOS\SAMPLES\POSUDEK\POSUDEK.docx"

def process_docx_document(read_file_path):
    document = docx.Document(read_file_path)

    whole_text = str()
    for index, content in enumerate(document.paragraphs):
        whole_text += content.text + "\r\n"

    
    return whole_text

process_docx_document(read_file_path)