import pickle


class FileManagement():
    temp_dict_file = []

    def __init__(self):

        with open('config.dictionary', 'rb') as config_dictionary_file:
            FileManagement.config_dictionary = pickle.load(
                config_dictionary_file)
        FileManagement.temp_dict_file = FileManagement.config_dictionary

    @classmethod
    def dump_file(cls):
        with open('config.dictionary', 'wb') as config_dictionary_file:
            pickle.dump(cls.temp_dict_file, config_dictionary_file)

    @classmethod
    def show_info(cls):
        i = 0
        for obj in cls.config_dictionary:
            print(i, ":", obj.name, "-", obj.second_name, "|Gender:",
                  obj.gender, "|Balance:", obj.balance)
            i += 1
