# File Exterminator

A CLI-based Python tool that allows you to completely wipe a file from disk, possibly rendering file recovery tools and techniques useless.
The project is currently under development.


## Getting Started
Follow these steps to setup this project on your machine.

1. Clone this repository:
```sh
git clone https://github.com/Kshitij-Jande/file-exterminator.git
```
2. Navigate to the cloned directory:
```sh
cd file-exterminator
```
3. Run the program (this prints the command usage)
```sh
py main.py
```


## Adding Custom Methods (Template)
To make things flexible, you can create and plug-in your own methods to deal with files, without any trouble of registering it manually. Follow these steps.

1. Create a new file under `methods` directory.
2. Paste in the following template:
```py
# Make sure that the class name is "Method".
class Method:
    def __init__(self):
        # Here, you can specify a name for your method.
        self.name = "Guttman Method"
        # You can write some description to tell what this module does.
        self.description = "Use the Guttman method to securely delete a file."

    # Make sure this function exists.
    def erase_file(self, path_to_file):
        # Write your code to deal with a file (using its path 'path_to_file').
        os.remove(path_to_file)

```
3. At this point, you are ready with your new method. It will automatically be registered by the program.
4. List all the available methods, you should see it listed:
```sh
py main.py list
```


## Wishlist
These are some enhancements and features that I aim to add to this project, in the future. Striked out items indicate that they have been implemented.

- ~~**Dynamic/Pluggable Method**: Make various overwriting methods register dynamically, allowing anyone to add their own method and plug it in.~~
- **Good error handling**: Common errors aren't handled, making it less user-friendly.
- ...


## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
If you like this project, you can give it a star. Thanks.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature`)
5. Open a Pull Request


## Acknowledgements
These are the references and resources I used to craft this project.

- [Explanation on the DoD 5220.22-M standard](https://www.jetico.com/blog/dod-522022-m-explained-data-erasure-standards)
- [Gutmann method](https://en.wikipedia.org/wiki/Gutmann_method)