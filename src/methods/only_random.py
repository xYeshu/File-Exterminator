import os
import random


class Method:
    def __init__(self):
        self.name = "Only Random"
        self.description = "Write random bytes and delete the file."

    def erase_file(self, path_to_file):
        orig_size = os.path.getsize(path_to_file)
        with open(path_to_file, 'wb') as f:
            random_data = bytes([random.randint(0, 255)
                                for i in range(orig_size)])
            f.write(random_data)
