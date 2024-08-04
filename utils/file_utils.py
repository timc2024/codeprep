import os

def get_common_path(paths):
    return os.path.commonpath(paths)

def get_relative_path(path, base_path):
    return os.path.relpath(path, base_path)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()