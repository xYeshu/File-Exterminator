import argparse
from file_deletion import FileDeletion


def main():
    parser = argparse.ArgumentParser(
        description='File Exterminator', add_help=False)
    parser.add_argument(
        '-h', action="help", help="Show help message. Use 'main.py <sub-command> -h' for sub-command help.")
    parser.add_argument(
        '-m', metavar="", help="Choose a method to erase data. Only available under 'delete' sub-command.")

    subparsers = parser.add_subparsers(
        title="Sub-Commands", metavar="", dest="subcommand")

    list_parser = subparsers.add_parser(
        "list", help="List all available erasure methods.")

    delete_parser = subparsers.add_parser(
        "delete", help="Delete a file securely.")
    delete_parser.add_argument("file", help="File to securely deleted.")
    delete_parser.add_argument(
        "-m", metavar="", help="Specify the ID of method to use.", dest="method")

    args = parser.parse_args()

    deleter = FileDeletion()

    if args.subcommand == "list":
        print("Below is a list of methods available.\n")
        for method in deleter.get_methods():
            print(f"ID: {method['id']}")
            print(f"Name: {method['name']}")
            print(f"Description: {method['description']}\n")
    elif args.subcommand == "delete":
        try:
            method_id = args.method
        except:
            method_id = "us_dod_5220"
        if not any(m.get('id') == method_id for m in deleter.get_methods()):
            print(f"Method with ID {method_id} not found.")
            return
        deleter.securely_delete(method_id, args.file)
        print(f"File {args.file} successfully erased using method {method_id}.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
