import tkinter
from tkinter import filedialog
from tkinter import *

from convert import convert

class GUI():
    def __init__(self, dos_dir_path, dosbox_path):
        self.dos_dir_path = "C:\DOS"
        self.dosbox_path = "C:\Program Files (x86)\DOSBox-0.74-3\DOSBox.exe"

        self.tb_len_int = 6
        self.lm_int = 1
        self.rm_int = 65
        self.pl_int = 55
        self.mt_int = 3
        self.mb_int = 3
        self.po_int = 5
        self.pn_int = 1

        self.root = tkinter.Tk()
        self.root.title("Convert602")

        self.path_label = tkinter.Label(self.root, text="Vstupní soubor").grid(row=0, column=0)
        self.path_to_input_entry = tkinter.Entry(self.root)
        self.path_to_input_entry.grid(row=0, column=1)
        self.browse_button = tkinter.Button(self.root, text="Vyber soubor", command=self.get_path_to_input_file)
        self.browse_button.grid(row=0, column=2)

        self.output_file_label = tkinter.Label(self.root, text="Název výstupního souboru").grid(row=1, column=0)
        self.output_file_name_entry = tkinter.Entry(self.root)
        self.output_file_name_entry.grid(row=1, column=1)

        self.tb_label = tkinter.Label(self.root, text="Délka tabelátoru").grid(row=3, column=0)
        self.tb_entry = tkinter.Entry(self.root, state="readonly")
        self.tb_entry.grid(row=3, column=1)
        self.lm_label = tkinter.Label(self.root, text="Levý okraj").grid(row=4, column=0)
        self.lm_entry = tkinter.Entry(self.root, state="readonly")
        self.lm_entry.grid(row=4, column=1)
        self.rm_label = tkinter.Label(self.root, text="Pravý okraj").grid(row=5, column=0)
        self.rm_entry = tkinter.Entry(self.root, state="readonly")
        self.rm_entry.grid(row=5, column=1)
        self.pl_label = tkinter.Label(self.root, text="Délka stránky").grid(row=6, column=0)
        self.pl_entry = tkinter.Entry(self.root, state="readonly")
        self.pl_entry.grid(row=6, column=1)
        self.mt_label = tkinter.Label(self.root, text="Horní okraj").grid(row=7, column=0)
        self.mt_entry = tkinter.Entry(self.root, state="readonly")
        self.mt_entry.grid(row=7, column=1)
        self.mb_label = tkinter.Label(self.root, text="Spodní okraj").grid(row=8, column=0)
        self.mb_entry = tkinter.Entry(self.root, state="readonly")
        self.mb_entry.grid(row=8, column=1)
        self.po_label = tkinter.Label(self.root, text="Tisk od sloupce").grid(row=9, column=0)
        self.po_entry = tkinter.Entry(self.root, state="readonly")
        self.po_entry.grid(row=9, column=1)
        self.pn_label = tkinter.Label(self.root, text="Tisk od stránky").grid(row=10, column=0)
        self.pn_entry = tkinter.Entry(self.root, state="readonly")
        self.pn_entry.grid(row=10, column=1)

        self.set_default_values()        

        self.adjust_label = tkinter.Label(self.root, text="Upřesnit parametry souboru T602").grid(row=2, column=0)
        self.state_int = IntVar()
        self.adjust_checkbutton = tkinter.Checkbutton(self.root, variable=self.state_int, onvalue=1, offvalue=0, command=self.change_visibilty_state)
        self.adjust_checkbutton.grid(row=2, column=1)

        self.run_conversion_button = tkinter.Button(self.root, text="Provést převod", command=self.run_conversion)
        self.run_conversion_button.grid(row=11, column=1)

        self.storno_button = tkinter.Button(self.root, text="Storno", command=self.destroy_window)
        self.storno_button.grid(row=11, column=2)

        self.root.mainloop()

    def change_visibilty_state(self):
        if self.state_int.get() == 1:
            self.set_state_normal()
        elif self.state_int.get() == 0:
            self.set_default_values()

    def run_conversion(self):
        input_file_path = self.path_to_input_entry.get()
        output_file_name = self.output_file_name_entry.get()

        tb_len_int = int(self.tb_entry.get())
        lm_int = int(self.lm_entry.get())
        rm_int = int(self.rm_entry.get())
        pl_int = int(self.pl_entry.get())
        mt_int = int(self.mt_entry.get())
        mb_int = int(self.mb_entry.get())
        po_int = int(self.po_entry.get())
        pn_int = int(self.pn_entry.get())

        convert(input_file_path, output_file_name, self.dos_dir_path, self.dosbox_path,
        tb_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int)

    def destroy_window(self):
        self.root.destroy()
    
    def set_default_values(self):
        self.set_state_normal()
        self.tb_entry.delete(0, "end")
        self.tb_entry.insert(0, str(self.tb_len_int))
        self.lm_entry.delete(0, "end")
        self.lm_entry.insert(0, str(self.lm_int))
        self.rm_entry.delete(0, "end")
        self.rm_entry.insert(0, str(self.rm_int))
        self.pl_entry.delete(0, "end")
        self.pl_entry.insert(0, str(self.pl_int))
        self.mt_entry.delete(0, "end")
        self.mt_entry.insert(0, str(self.mt_int))
        self.mb_entry.delete(0, "end")
        self.mb_entry.insert(0, str(self.mb_int))
        self.po_entry.delete(0, "end")
        self.po_entry.insert(0, str(self.po_int))
        self.pn_entry.delete(0, "end")
        self.pn_entry.insert(0, str(self.pn_int))
        self.set_state_readonly()

    def set_state_normal(self):
        self.tb_entry.config(state="normal")
        self.lm_entry.config(state="normal")
        self.rm_entry.config(state="normal")
        self.pl_entry.config(state="normal")
        self.mt_entry.config(state="normal")
        self.mb_entry.config(state="normal")
        self.po_entry.config(state="normal")
        self.pn_entry.config(state="normal")

    def set_state_readonly(self):
        self.tb_entry.config(state="readonly")
        self.lm_entry.config(state="readonly")
        self.rm_entry.config(state="readonly")
        self.pl_entry.config(state="readonly")
        self.mt_entry.config(state="readonly")
        self.mb_entry.config(state="readonly")
        self.po_entry.config(state="readonly")
        self.pn_entry.config(state="readonly")
    
    def get_path_to_input_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/" ,title = "Select file",filetypes = (("docx files","*.docx"),("PDF files","*.pdf")))
        self.path_to_input_entry.delete(0, "end")
        self.path_to_input_entry.insert(0, self.filename)