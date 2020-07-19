import tkinter
from tkinter import *

class GUI():
    def __init__(self):
        self.root = tkinter.Tk()
        self.path_label = tkinter.Label(self.root, text="Vstupní soubor").grid(row=0, column=0)
        self.path_to_input_entry = tkinter.Entry(self.root)
        self.path_to_input_entry.grid(row=0, column=1)
        self.browse_button = tkinter.Button(self.root, text="Vyber soubor")
        self.browse_button.grid(row=0, column=2)

        self.output_file_label = tkinter.Label(self.root, text="Název výstupního souboru").grid(row=1, column=0)
        self.output_file_name_entry = tkinter.Entry(self.root)
        self.output_file_name_entry.grid(row=1, column=1)

        self.lm_label = tkinter.Label(self.root, text="Levý okraj").grid(row=3, column=0)
        self.lm_entry = tkinter.Entry(self.root, state="disabled")
        self.lm_entry.grid(row=3, column=1)
        self.rm_label = tkinter.Label(self.root, text="Pravý okraj").grid(row=4, column=0)
        self.rm_entry = tkinter.Entry(self.root, state="disabled")
        self.rm_entry.grid(row=4, column=1)
        self.pl_label = tkinter.Label(self.root, text="Délka stránky").grid(row=5, column=0)
        self.pl_entry = tkinter.Entry(self.root, state="disabled")
        self.pl_entry.grid(row=5, column=1)
        self.mt_label = tkinter.Label(self.root, text="Horní okraj").grid(row=6, column=0)
        self.mt_entry = tkinter.Entry(self.root, state="disabled")
        self.mt_entry.grid(row=6, column=1)
        self.mb_label = tkinter.Label(self.root, text="Spodní okraj").grid(row=7, column=0)
        self.mb_entry = tkinter.Entry(self.root, state="disabled")
        self.mb_entry.grid(row=7, column=1)
        self.po_label = tkinter.Label(self.root, text="Tisk od sloupce").grid(row=8, column=0)
        self.po_entry = tkinter.Entry(self.root, state="disabled")
        self.po_entry.grid(row=8, column=1)
        self.pn_label = tkinter.Label(self.root, text="Tisk od stránky").grid(row=9, column=0)
        self.pn_entry = tkinter.Entry(self.root, state="disabled")
        self.pn_entry.grid(row=9, column=1)

        self.adjust_label = tkinter.Label(self.root, text="Upřesnit parametry souboru T602").grid(row=2, column=0)
        self.state_int = IntVar()
        self.adjust_checkbutton = tkinter.Checkbutton(self.root, variable=self.state_int, onvalue=1, offvalue=0, command=self.change_visibilty_state)
        self.adjust_checkbutton.grid(row=2, column=1)

        self.run_conversion_button = tkinter.Button(self.root, text="Provést převod", command=self.run_conversion)
        self.run_conversion_button.grid(row=10, column=1)

        self.storno_button = tkinter.Button(self.root, text="Storno", command=self.destroy_window)
        self.storno_button.grid(row=10, column=2)

        self.root.mainloop()

    def change_visibilty_state(self):
        if self.state_int.get() == 1:
            self.lm_entry.config(state="normal")
            self.rm_entry.config(state="normal")
            self.pl_entry.config(state="normal")
            self.mt_entry.config(state="normal")
            self.mb_entry.config(state="normal")
            self.po_entry.config(state="normal")
            self.pn_entry.config(state="normal")
        elif self.state_int.get() == 0:
            self.lm_entry.config(state="disabled")
            self.rm_entry.config(state="disabled")
            self.pl_entry.config(state="disabled")
            self.mt_entry.config(state="disabled")
            self.mb_entry.config(state="disabled")
            self.po_entry.config(state="disabled")
            self.pn_entry.config(state="disabled")

    def run_conversion(self):
        pass

    def destroy_window(self):
        self.root.destroy()

gui = GUI()