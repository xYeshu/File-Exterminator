import os


class Method:
    def __init__(self):
        self.name = "Pure Zeros"
        self.description = "Write only zeros (0s) and delete the file."

    def erase_file(self, path_to_file):
        orig_size = os.path.getsize(path_to_file)
        with open(path_to_file, 'wb') as f:
            f.write(b'\x00' * orig_size)
        os.remove(path_to_file)
