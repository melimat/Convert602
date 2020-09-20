import configparser
import os

class Config_handler():
    def __init__(self):
        appdata_path = os.getenv("APPDATA")

        print(appdata_path)

        self.config_dir_path = os.path.join(appdata_path, "Convert602")
        self.config_file_path = os.path.join(self.config_dir_path, "convert602.ini")

        self.sample_config = configparser.ConfigParser(allow_no_value=True)
        
        self.sample_config["App"] = {"language" : ""}
        self.sample_config["DOSBox"] = {"dos_dir_path" : "", "dosbox_app_path" : ""}
        self.sample_config["Text_segmentation"] = {"chars_limit" : ""}

        if os.path.exists(self.config_file_path):
            self.read_config()
        else:
            if os.path.isdir(self.config_dir_path) == False:
                os.mkdir(self.config_dir_path)
            
            self.write_config("", "", "260000", "EN")


    def write_config(self, dos_dir_path, dosbox_app_path, chars_limit, language):
        self.sample_config["DOSBox"]["dos_dir_path"] = dos_dir_path
        self.sample_config["DOSBox"]["dosbox_app_path"] = dosbox_app_path
        self.sample_config["Text_segmentation"]["chars_limit"] = chars_limit
        self.sample_config["App"]["language"] = language

        with open(self.config_file_path, "w") as config_file:
            self.sample_config.write(config_file)
        
        self.read_config()

    def read_config(self):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(self.config_file_path)

        self.dos_dir_path = config["DOSBox"]["dos_dir_path"]
        self.dosbox_path = config["DOSBox"]["dosbox_app_path"]
        self.chars_limit = config["Text_segmentation"]["chars_limit"]
        self.language = config["App"]["language"]

        if len(self.dos_dir_path) == 0 or len(self.dosbox_path) == 0 or len(self.chars_limit) == 0:
            self.incomplete_config = True
        else:
            self.incomplete_config = False
