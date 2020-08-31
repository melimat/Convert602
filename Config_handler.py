import configparser
import os

class Config_handler():
    def __init__(self, config_file_name):
        self.config_file_name = config_file_name

        self.sample_config = configparser.ConfigParser(allow_no_value=True)

        self.sample_config["DOSBox"] = {"dos_dir_path" : "", "dosbox_app_path" : ""}
        self.sample_config["Text_segmentation"] = {"chars_limit" : ""}

        files_list = os.listdir()

        if (config_file_name in files_list):
            self.read_config()
        else:
            self.write_config("", "", "260000")

    def write_config(self, dos_dir_path, dosbox_app_path, chars_limit):
        self.sample_config["DOSBox"]["dos_dir_path"] = dos_dir_path
        self.sample_config["DOSBox"]["dosbox_app_path"] = dosbox_app_path
        self.sample_config["Text_segmentation"]["chars_limit"] = chars_limit

        with open(self.config_file_name, "w") as config_file:
            self.sample_config.write(config_file)
        
        self.read_config()

    def read_config(self):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(self.config_file_name)

        self.dos_dir_path = config["DOSBox"]["dos_dir_path"]
        self.dosbox_path = config["DOSBox"]["dosbox_app_path"]
        self.chars_limit = config["Text_segmentation"]["chars_limit"]

        if len(self.dos_dir_path) == 0 or len(self.dosbox_path) == 0 or len(self.chars_limit) == 0:
            self.incomplete_config = True
        else:
            self.incomplete_config = False
