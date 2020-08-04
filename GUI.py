import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

from convert import convert
from Config_handler import Config_handler

class GUI():
    def __init__(self):
        self.config = Config_handler("Convert602.ini")

        self.initial_dir = "/"

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

        self.open_dosbox_label = tkinter.Label(self.root, text="Otevřít DOSBox").grid(row=0, column=0)
        self.dosbox_state_int = IntVar(self.root)
        self.open_dosbox_checkbox = tkinter.Checkbutton(self.root, variable=self.dosbox_state_int, onvalue=1, offvalue=0, command=self.change_dosbox_state)
        self.open_dosbox_checkbox.grid(row=0, column=1)

        self.path_label = tkinter.Label(self.root, text="Vstupní soubor").grid(row=1, column=0)
        self.path_to_input_entry = tkinter.Entry(self.root)
        self.path_to_input_entry.grid(row=1, column=1)
        self.browse_input_button = tkinter.Button(self.root, text="Vyber soubor", command=self.get_path_to_input_file)
        self.browse_input_button.grid(row=1, column=2)

        self.output_file_label = tkinter.Label(self.root, text="Výstupní soubor").grid(row=2, column=0)
        self.output_file_path_entry = tkinter.Entry(self.root)
        self.output_file_path_entry.grid(row=2, column=1)
        self.browse_output_button = tkinter.Button(self.root, text="Vyber soubor", command=self.get_path_to_output_file)
        self.browse_output_button.grid(row=2, column=2)

        self.tb_label = tkinter.Label(self.root, text="Délka tabelátoru").grid(row=4, column=0)
        self.tb_entry = tkinter.Entry(self.root, state="readonly")
        self.tb_entry.grid(row=4, column=1)
        self.lm_label = tkinter.Label(self.root, text="Levý okraj").grid(row=5, column=0)
        self.lm_entry = tkinter.Entry(self.root, state="readonly")
        self.lm_entry.grid(row=5, column=1)
        self.rm_label = tkinter.Label(self.root, text="Pravý okraj").grid(row=6, column=0)
        self.rm_entry = tkinter.Entry(self.root, state="readonly")
        self.rm_entry.grid(row=6, column=1)
        self.pl_label = tkinter.Label(self.root, text="Délka stránky").grid(row=7, column=0)
        self.pl_entry = tkinter.Entry(self.root, state="readonly")
        self.pl_entry.grid(row=7, column=1)
        self.mt_label = tkinter.Label(self.root, text="Horní okraj").grid(row=8, column=0)
        self.mt_entry = tkinter.Entry(self.root, state="readonly")
        self.mt_entry.grid(row=8, column=1)
        self.mb_label = tkinter.Label(self.root, text="Spodní okraj").grid(row=9, column=0)
        self.mb_entry = tkinter.Entry(self.root, state="readonly")
        self.mb_entry.grid(row=9, column=1)
        self.po_label = tkinter.Label(self.root, text="Tisk od sloupce").grid(row=10, column=0)
        self.po_entry = tkinter.Entry(self.root, state="readonly")
        self.po_entry.grid(row=10, column=1)
        self.pn_label = tkinter.Label(self.root, text="Tisk od stránky").grid(row=11, column=0)
        self.pn_entry = tkinter.Entry(self.root, state="readonly")
        self.pn_entry.grid(row=11, column=1)

        self.set_default_values()        

        self.adjust_label = tkinter.Label(self.root, text="Upřesnit parametry souboru T602").grid(row=3, column=0)
        self.state_int = IntVar()
        self.adjust_checkbutton = tkinter.Checkbutton(self.root, variable=self.state_int, onvalue=1, offvalue=0, command=self.change_visibilty_state)
        self.adjust_checkbutton.grid(row=3, column=1)

        self.settings_button = tkinter.Button(self.root, text="Nastavení", command=self.settings_window)
        self.settings_button.grid(row=12, column=0)

        self.run_conversion_button = tkinter.Button(self.root, text="Provést převod", command=self.run_conversion)
        self.run_conversion_button.grid(row=12, column=1)

        self.storno_button = tkinter.Button(self.root, text="Storno", command=self.destroy_window)
        self.storno_button.grid(row=12, column=2)

        self.root.mainloop()

    def change_visibilty_state(self):
        if self.state_int.get() == 1:
            self.set_state_normal()
        elif self.state_int.get() == 0:
            self.set_default_values()

    def change_dosbox_state(self):
        if self.dosbox_state_int.get() == 1:
            self.initial_dir = self.config.dos_dir_path
            self.open_dosbox_bool = True
        elif self.dosbox_state_int.get() == 0:
            self.initial_dir = "/"
            self.open_dosbox_bool = False

    def run_conversion(self):
        input_file_path = self.path_to_input_entry.get()
        output_file_path = self.output_file_path_entry.get()

        tb_len_int = int(self.tb_entry.get())
        lm_int = int(self.lm_entry.get())
        rm_int = int(self.rm_entry.get())
        pl_int = int(self.pl_entry.get())
        mt_int = int(self.mt_entry.get())
        mb_int = int(self.mb_entry.get())
        po_int = int(self.po_entry.get())
        pn_int = int(self.pn_entry.get())

        if self.config.incomplete_config == True and self.open_dosbox_bool == True:
            messagebox.showerror("Error", "Konfigurace programu není kompletní, upřesni v nastavení.")
            return
        
        convert(self.open_dosbox_bool, input_file_path, output_file_path, self.config.dos_dir_path, self.config.dosbox_path,
        tb_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int)

        if self.open_dosbox_bool == False:
            messagebox.showinfo("Konverze dokončena", "Konverze dokončena")

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
        filename = filedialog.askopenfilename(initialdir="/" ,title = "Select file",filetypes = (("docx files","*.docx"),("PDF files","*.pdf")))
        self.path_to_input_entry.delete(0, "end")
        self.path_to_input_entry.insert(0, filename)

    def get_path_to_output_file(self):
        output_file_path = filedialog.asksaveasfilename(initialdir=self.initial_dir, filetypes=[("T602 Files", '*.602')])
        if ".602" not in output_file_path and len(output_file_path) !=0:
            output_file_path += ".602"
        self.output_file_path_entry.delete(0, "end")
        self.output_file_path_entry.insert(0, output_file_path)
    
    def settings_window(self):
        self.top = tkinter.Toplevel(self.root)

        self.top.title("Možnosti")

        dosbox_path_label = tkinter.Label(self.top, text="Aplikace dosbox").grid(row=0, column=0)
        self.dosbox_path_entry = tkinter.Entry(self.top)
        self.dosbox_path_entry.grid(row=0, column=1)
        self.dosbox_path_entry.insert(0, self.config.dosbox_path)
        dosbox_path_browse_button = tkinter.Button(self.top, text="Vyber soubor", command=self.get_dosbox_path)
        dosbox_path_browse_button.grid(row=0, column=2)

        dos_dir_label = tkinter.Label(self.top, text="Kořenový adresář DOS").grid(row=1, column=0)
        self.dos_dir_entry = tkinter.Entry(self.top)
        self.dos_dir_entry.grid(row=1, column=1)
        self.dos_dir_entry.insert(0, self.config.dos_dir_path)
        dos_dir_browse_button = tkinter.Button(self.top, text="Vyber adresář", command=self.get_dos_dir)
        dos_dir_browse_button.grid(row=1, column=2)

        apply_settings_button = tkinter.Button(self.top, text="Aplikovat nastavení", command=self.apply_settings)
        apply_settings_button.grid(row=2, column=1)

        exit_settings_button = tkinter.Button(self.top, text="Storno", command=self.exit_settings)
        exit_settings_button.grid(row=2, column=2)
    
    def get_dosbox_path(self):
        dosbox_path = filedialog.askopenfilename(initialdir="/" ,title = "Select file",filetypes = [("executable files","*.exe")])
        self.dosbox_path_entry.delete(0, "end")
        self.dosbox_path_entry.insert(0, dosbox_path)

    def get_dos_dir(self):
        dos_dir_path = filedialog.askdirectory()
        self.dos_dir_entry.delete(0, "end")
        self.dos_dir_entry.insert(0, dos_dir_path)

    def apply_settings(self):
        dos_dir_path = self.dos_dir_entry.get()
        dosbox_path = self.dosbox_path_entry.get()

        self.config.write_config(dos_dir_path, dosbox_path)
        self.exit_settings()

    def exit_settings(self):
        self.top.destroy()

