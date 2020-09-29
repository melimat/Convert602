class Localistions():
    def __init__(self):
        czech_lang = {
            "open_dosbox_label" : "Otevřít DOSBox",
            "path_to_input_label" : "Vstupní soubor",
            "browse_for_file_button_text" : "Vyber soubor",
            "path_to_output_label" : "Výstupní soubor",
            "tb_len_label" : "Délka tabulátoru",
            "lm_label" : "Levý okraj",
            "rm_label" : "Pravý okraj",
            "pl_label" : "Délka strany",
            "mt_label" : "Horní okraj",
            "mb_label" : "Spodní okraj",
            "po_label" : "Tisk od sloupce",
            "pn_label" : "Tisk od stránky",
            "adjust_label" : "Upřesnit parametry souboru T602",
            "settings_button_text" : "Nastavení",
            "run_conversion_button_text" : "Provést převod",
            "competition_text" : "Toto je soutěžní aplikce\n v soutěži ITnetwork summer 2020",
            "message_config_not_complete" : "Konfigurace programu není kompletní, upřesni v nastavení.",
            "message_conversion_finished" : "Konverze dokončena",
            "options_window_title" : "Možnosti",
            "dosbox_path_label" : "Aplikace dosbox",
            "dos_dir_label" : "Kořenvý adresář DOS",
            "browse_for_dir_button_text" : "Vyber adresář",
            "chars_limit_label" : "Maximální počet znaků pro T602 soubor",
            "reset_chars_limit_button_text" : "Nastavit výchozí hodnotu",
            "language_label" : "Jazyk",
            "apply_settings_button_text" : "Aplikovat nastavení"
        }

        english_lang = {
            "open_dosbox_label" : "Open DOSBox",
            "path_to_input_label" : "Input file",
            "browse_for_file_button_text" : "Choose file",
            "path_to_output_label" : "Output file",
            "tb_len_label" : "Tabulator length",
            "lm_label" : "Left margin",
            "rm_label" : "Right margin",
            "pl_label" : "Page length",
            "mt_label" : "Top margin",
            "mb_label" : "Bottom margin",
            "po_label" : "Print from column",
            "pn_label" : "Print from page",
            "adjust_label" : "Adjust T602 file parameters",
            "settings_button_text" : "Settings",
            "run_conversion_button_text" : "Run conversion",
            "competition_text" : "This app is made for competition\n ITnetwork Summer 2020",
            "message_config_not_complete" : "Configuration of the app is not complete, please complete the configuration in Settings",
            "message_conversion_finished" : "Conversion finished",
            "options_window_title" : "Settings",
            "dosbox_path_label" : "Dosbox app",
            "dos_dir_label" : "Root DOS directory",
            "browse_for_dir_button_text" : "Choose directory",
            "chars_limit_label" : "Maximal number of characters for T602 file",
            "reset_chars_limit_button_text" : "Reset to default value",
            "language_label" : "Language",
            "apply_settings_button_text" : "Apply settings"
        }

        self.languages_dict = {
            "CZ" : czech_lang,
            "EN" : english_lang
        }
