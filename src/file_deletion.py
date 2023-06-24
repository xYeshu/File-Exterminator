import os
import importlib


class FileDeletion:
    def __init__(self):
        self.methods = {}
        self.register_methods()

    def register_methods(self):
        folder = "methods"
        methods = os.listdir(folder)

        for file in methods:
            if not file.endswith(".py"):
                continue
            name = file[:-3]
            path = os.path.join(folder, file)
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            method_class = getattr(module, "Method")
            if not method_class:
                continue
            method_instance = method_class()
            self.methods[name] = method_instance

    def get_methods(self):
        methods_info = []
        for file, method in self.methods.items():
            methods_info.append(
                {
                    'id': file,
                    'name': method.name,
                    'description': method.description
                }
            )
        return methods_info

    def securely_delete(self, method_id, path_to_file):
        if method_id not in self.methods:
            raise Exception("Method with that ID not found.")

        method = self.methods[method_id]
        method.erase_file(path_to_file)