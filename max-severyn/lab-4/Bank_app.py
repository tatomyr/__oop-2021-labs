import os
from MenuManagement import MenuManagement
from FileManagement import *
from Switch import Switch


if not os.path.exists("config.dictionary"):
    FileManagement.dump_file()

    FileManagement()
    MenuManagement.static_menu()
    Switch.input_number()
    FileManagement.dump_file()

else:
    FileManagement()
    MenuManagement.static_menu()
    Switch.input_number()
    FileManagement.dump_file()
