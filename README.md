FDIO is a Python command line interface (CLI) tool designed to allow you to manage your files and directories.


## Features:

File Manager CLI Tool.

A command line utility (CLI) for file and directory operations.
Provides commands to: 

- List files.
- Create directories and files.
- Purge files and directories.
- Display file contents.


## Commands:

- List files and directories.

Lists all files and directories in the current directory or specified paths.

Arguments:
paths (tuple of Path): Paths to list. If no paths are provided, lists the contents of the current directory.

Examples:

    flio lfd

    flio lfd /path/to/directory-1 /path/to/directory-2 ...


- Create directories.

Creates one or more directories.

Arguments:
path (tuple of Path): Paths to directories to be created. If directories already exist, they are not modified.

Examples:

    flio crd new_directory another_directory ...


- Create files.

Creates one or more files in the current directory or specified path.

Arguments:
filename (tuple of File): Names of files to be created.
path (Path, optional): Custom path where the files will be created. If not provided, files are created in the current directory.

Examples:

    flio crf file1.txt file2.txt ...
    flio crf -p /path/to/directory file1.txt file2.txt ...


- Purge files and directories.

Deletes specified files and directories. Requires user confirmation.

Arguments:
paths (tuple of Path): Paths of files and directories to be deleted.

Examples:

    flio prg file1.txt directory1 ...


- Show file contents.

Displays the content of one or more files.

Arguments:
files (tuple of File): Files to display the contents of.

Examples:

    flio cnt file1.txt file2.txt
