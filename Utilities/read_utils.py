import pandas


def get_dic_from_json(file_path):
    dic = pandas.read_json(path_or_buf=file_path, typ="dictionary")
    return dic