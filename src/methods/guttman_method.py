import os


class Method:
    def __init__(self):
        self.name = "Guttman Method"
        self.description = "Use the Guttman method to securely delete a file."

    def erase_file(self, path_to_file):
        orig_size = os.path.getsize(path_to_file)

        with open(path_to_file, "rb+") as file:
            for pass_num in range(35):
                random_data = bytearray(orig_size)
                file.write(random_data)

        os.remove(path_to_file)
