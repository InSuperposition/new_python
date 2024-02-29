import os

def get_absolute_path(*paths) -> str:
    dirname = os.path.dirname(__file__)
    return os.path.normpath(os.path.join(dirname, *paths))
