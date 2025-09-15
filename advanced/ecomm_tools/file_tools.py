import os

def list_files(path="."):
    """Return all files in the given folder"""
    return [f for f in os.listdir(path) if os.path.isfile(f)]
