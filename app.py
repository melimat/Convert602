import sys

from GUI import GUI

dos_dir_path = sys.argv[1]
dosbox_path = sys.argv[2]

gui = GUI(dos_dir_path, dosbox_path)
