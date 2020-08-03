import configparser
import os

class Config_handler():
    def __init__(self, config_file_name):
        self.config_file_name = config_file_name

        self.sample_config = configparser.ConfigParser(allow_no_value=True)

        self.sample_config["DOSBox"] = {"dos_dir_path" : "", "dosbox_app_path" : ""}

        files_list = os.listdir()

        if (config_file_name in files_list):
            self.config_exists = True
        else:
            self.config_exists = False
            self.write_config("", "")

    def write_config(self, dos_dir_path, dosbox_app_path):
        self.sample_config["DOSBox"]["dos_dir_path"] = dos_dir_path
        self.sample_config["DOSBox"]["dosbox_app_path"] = dosbox_app_path

        with open(self.config_file_name, "w") as config_file:
            self.sample_config.write(config_file)

    def read_config(self):
        pass

cfg_handler = Config_handler("Convert602.ini")
