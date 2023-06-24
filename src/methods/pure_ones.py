import os


class Method:
    def __init__(self):
        self.name = "Pure Ones"
        self.description = "Write only ones (1s) and delete the file."

    def erase_file(self, path_to_file):
        orig_size = os.path.getsize(path_to_file)
        with open(path_to_file, 'wb') as f:
            f.write(b'\xFF' * orig_size)
        os.remove(path_to_file)
