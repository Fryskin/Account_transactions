import json


def read_json_file(path):
    """
    Reading file with info about transactions and returning content from file.
    :param path: file with transactions.
    :return: content from file.
    """
    with open(path, encoding='utf-8') as file:
        content = json.load(file)

        return content




