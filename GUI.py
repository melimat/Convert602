import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

import webbrowser

from convert import convert
from Config_handler import Config_handler
from Localisations import Localistions

class GUI():
    def __init__(self):
        self.config = Config_handler("Convert602.ini")
        self.localisations = Localistions() 

        self.initial_dir = "/"
        self.open_dosbox_bool = False

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

        self.open_dosbox_label = tkinter.Label(self.root)
        self.open_dosbox_label.grid(row=0, column=0)
        self.dosbox_state_int = IntVar(self.root)
        self.open_dosbox_checkbox = tkinter.Checkbutton(self.root, variable=self.dosbox_state_int, onvalue=1, offvalue=0, command=self.change_dosbox_state)
        self.open_dosbox_checkbox.grid(row=0, column=1)

        self.path_to_input_label = tkinter.Label(self.root)
        self.path_to_input_label.grid(row=1, column=0)
        self.path_to_input_entry = tkinter.Entry(self.root)
        self.path_to_input_entry.grid(row=1, column=1)
        self.browse_input_button = tkinter.Button(self.root, command=self.get_path_to_input_file)
        self.browse_input_button.grid(row=1, column=2)

        self.output_file_label = tkinter.Label(self.root)
        self.output_file_label.grid(row=2, column=0)
        self.output_file_path_entry = tkinter.Entry(self.root)
        self.output_file_path_entry.grid(row=2, column=1)
        self.browse_output_button = tkinter.Button(self.root, command=self.get_path_to_output_file)
        self.browse_output_button.grid(row=2, column=2)

        self.tb_label = tkinter.Label(self.root)
        self.tb_label.grid(row=4, column=0)
        self.tb_entry = tkinter.Entry(self.root, state="readonly")
        self.tb_entry.grid(row=4, column=1)
        self.lm_label = tkinter.Label(self.root)
        self.lm_label.grid(row=5, column=0)
        self.lm_entry = tkinter.Entry(self.root, state="readonly")
        self.lm_entry.grid(row=5, column=1)
        self.rm_label = tkinter.Label(self.root)
        self.rm_label.grid(row=6, column=0)
        self.rm_entry = tkinter.Entry(self.root, state="readonly")
        self.rm_entry.grid(row=6, column=1)
        self.pl_label = tkinter.Label(self.root)
        self.pl_label.grid(row=7, column=0)
        self.pl_entry = tkinter.Entry(self.root, state="readonly")
        self.pl_entry.grid(row=7, column=1)
        self.mt_label = tkinter.Label(self.root)
        self.mt_label.grid(row=8, column=0)
        self.mt_entry = tkinter.Entry(self.root, state="readonly")
        self.mt_entry.grid(row=8, column=1)
        self.mb_label = tkinter.Label(self.root)
        self.mb_label.grid(row=9, column=0)
        self.mb_entry = tkinter.Entry(self.root, state="readonly")
        self.mb_entry.grid(row=9, column=1)
        self.po_label = tkinter.Label(self.root)
        self.po_label.grid(row=10, column=0)
        self.po_entry = tkinter.Entry(self.root, state="readonly")
        self.po_entry.grid(row=10, column=1)
        self.pn_label = tkinter.Label(self.root)
        self.pn_label.grid(row=11, column=0)
        self.pn_entry = tkinter.Entry(self.root, state="readonly")
        self.pn_entry.grid(row=11, column=1)

        self.set_default_values()        

        self.adjust_label = tkinter.Label(self.root)
        self.adjust_label.grid(row=3, column=0)
        self.state_int = IntVar()
        self.adjust_checkbutton = tkinter.Checkbutton(self.root, variable=self.state_int, onvalue=1, offvalue=0, command=self.change_visibilty_state)
        self.adjust_checkbutton.grid(row=3, column=1)

        self.settings_button = tkinter.Button(self.root, command=self.settings_window)
        self.settings_button.grid(row=12, column=0)

        self.run_conversion_button = tkinter.Button(self.root, command=self.run_conversion)
        self.run_conversion_button.grid(row=12, column=1)

        self.storno_button = tkinter.Button(self.root, text="Storno", command=self.destroy_window)
        self.storno_button.grid(row=12, column=2)

        self.competition_text = tkinter.Label(self.root)
        self.competition_text.grid(row=13, column=0)
        self.itnetwork_url_link = tkinter.Label(self.root, text="https://www.itnetwork.cz/", fg="blue", cursor="hand2")
        self.itnetwork_url_link.bind("<Button-1>",lambda e: self.itnetwork_url_callback())
        self.itnetwork_url_link.grid(row=13, column=1)

        self.populate_all_main_window_text()

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
        chars_limit = int(self.config.chars_limit)

        if self.config.incomplete_config == True and self.open_dosbox_bool == True:
            messagebox.showerror("Error", self.localisations.languages_dict[self.config.language]["message_config_not_complete"])
            return
        
        convert(self.open_dosbox_bool, chars_limit, input_file_path, output_file_path, self.config.dos_dir_path,
        self.config.dosbox_path, tb_len_int, lm_int, rm_int, pl_int, mt_int, mb_int, po_int, pn_int)

        if self.open_dosbox_bool == False:
            completed_message = self.localisations.languages_dict[self.config.language]["message_conversion_finished"]
            messagebox.showinfo(completed_message, completed_message)

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

        self.top.title(self.localisations.languages_dict[self.config.language]["options_window_title"])

        self.dosbox_path_label = tkinter.Label(self.top)
        self.dosbox_path_label.grid(row=0, column=0)
        self.dosbox_path_entry = tkinter.Entry(self.top)
        self.dosbox_path_entry.grid(row=0, column=1)
        self.dosbox_path_entry.insert(0, self.config.dosbox_path)
        self.dosbox_path_browse_button = tkinter.Button(self.top, command=self.get_dosbox_path)
        self.dosbox_path_browse_button.grid(row=0, column=2)

        self.dos_dir_label = tkinter.Label(self.top)
        self.dos_dir_label.grid(row=1, column=0)
        self.dos_dir_entry = tkinter.Entry(self.top)
        self.dos_dir_entry.grid(row=1, column=1)
        self.dos_dir_entry.insert(0, self.config.dos_dir_path)
        self.dos_dir_browse_button = tkinter.Button(self.top, command=self.get_dos_dir)
        self.dos_dir_browse_button.grid(row=1, column=2)

        self.chars_limit_label = tkinter.Label(self.top)
        self.chars_limit_label.grid(row=2, column=0)
        self.chars_limit_entry = tkinter.Entry(self.top)
        self.chars_limit_entry.grid(row=2, column=1)
        self.chars_limit_entry.insert(0, self.config.chars_limit)
        self.reset_chars_limit_button = tkinter.Button(self.top, command=self.set_default_chars_limit)
        self.reset_chars_limit_button.grid(row=2, column=2)

        self.language_label = tkinter.Label(self.top)
        self.language_label.grid(row=3, column=0)
        self.language_var = StringVar(self.top)
        choices = self.localisations.languages_dict.keys()
        self.language_var.set(self.config.language)
        self.language_dropdown = tkinter.OptionMenu(self.top, self.language_var, *choices)
        self.language_dropdown.grid(row=3, column=1)

        self.apply_settings_button = tkinter.Button(self.top, command=self.apply_settings)
        self.apply_settings_button.grid(row=4, column=1)

        exit_settings_button = tkinter.Button(self.top, text="Storno", command=self.exit_settings)
        exit_settings_button.grid(row=4, column=2)

        self.populate_all_settings_window_text()
    
    def get_dosbox_path(self):
        dosbox_path = filedialog.askopenfilename(initialdir="/" ,title = "Select file",filetypes = [("executable files","*.exe"), ("all files", "*.*")])
        self.dosbox_path_entry.delete(0, "end")
        self.dosbox_path_entry.insert(0, dosbox_path)

    def get_dos_dir(self):
        dos_dir_path = filedialog.askdirectory()
        self.dos_dir_entry.delete(0, "end")
        self.dos_dir_entry.insert(0, dos_dir_path)

    def apply_settings(self):
        dos_dir_path = self.dos_dir_entry.get()
        dosbox_path = self.dosbox_path_entry.get()
        chars_limit = self.chars_limit_entry.get()
        language = self.language_var.get()

        self.config.write_config(dos_dir_path, dosbox_path, chars_limit, language)

        self.populate_all_main_window_text()

        self.exit_settings()

    def exit_settings(self):
        self.top.destroy()

    def itnetwork_url_callback(self):
        webbrowser.open_new("https://www.itnetwork.cz/")

    def set_default_chars_limit(self):
        self.chars_limit_entry.delete(0, "end")
        self.chars_limit_entry.insert(0, "260000")

    def populate_all_main_window_text(self):
        language = self.config.language

        self.open_dosbox_label.configure(text=self.localisations.languages_dict[language]["open_dosbox_label"])
        self.path_to_input_label.configure(text=self.localisations.languages_dict[language]["path_to_input_label"])
        self.browse_input_button.configure(text=self.localisations.languages_dict[language]["browse_for_file_button_text"])
        self.output_file_label.configure(text=self.localisations.languages_dict[language]["path_to_output_label"])
        self.browse_output_button.configure(text=self.localisations.languages_dict[language]["browse_for_file_button_text"])
        self.tb_label.configure(text=self.localisations.languages_dict[language]["tb_len_label"])
        self.lm_label.configure(text=self.localisations.languages_dict[language]["lm_label"])
        self.rm_label.configure(text=self.localisations.languages_dict[language]["rm_label"])
        self.pl_label.configure(text=self.localisations.languages_dict[language]["pl_label"])
        self.mt_label.configure(text=self.localisations.languages_dict[language]["mt_label"])
        self.mb_label.configure(text=self.localisations.languages_dict[language]["mb_label"])
        self.po_label.configure(text=self.localisations.languages_dict[language]["po_label"])
        self.pn_label.configure(text=self.localisations.languages_dict[language]["pn_label"])
        self.adjust_label.configure(text=self.localisations.languages_dict[language]["adjust_label"])
        self.settings_button.configure(text=self.localisations.languages_dict[language]["settings_button_text"])
        self.run_conversion_button.configure(text=self.localisations.languages_dict[language]["run_conversion_button_text"])
        self.competition_text.configure(text=self.localisations.languages_dict[language]["competition_text"])

    def populate_all_settings_window_text(self):
        language = self.config.language

        self.dosbox_path_label.configure(text=self.localisations.languages_dict[language]["dosbox_path_label"])
        self.dosbox_path_browse_button.configure(text=self.localisations.languages_dict[language]["browse_for_file_button_text"])
        self.dos_dir_label.configure(text=self.localisations.languages_dict[language]["dos_dir_label"])
        self.dos_dir_browse_button.configure(text=self.localisations.languages_dict[language]["browse_for_dir_button_text"])
        self.chars_limit_label.configure(text=self.localisations.languages_dict[language]["chars_limit_label"])
        self.reset_chars_limit_button.configure(text=self.localisations.languages_dict[language]["reset_chars_limit_button_text"])
        self.language_label.configure(text=self.localisations.languages_dict[language]["language_label"])
        self.apply_settings_button.configure(text=self.localisations.languages_dict[language]["apply_settings_button_text"])

