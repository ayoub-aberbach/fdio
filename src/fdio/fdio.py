from pathlib import Path
import click
import sys

from fdio.utils import delete_folder


@click.group()
@click.version_option("1.01")
def cli():
    """
    File Manager CLI Tool.

    A command line utility (CLI) for file and directory operations.
    Provides commands to list files, create directories and files,
    purge files and directories, and display file contents.
    """
    pass


@cli.command(help="List all files and directories of a given path.")
@click.argument("paths", nargs=-1, type=click.Path(exists=True, file_okay=True, readable=True, path_type=Path))
def lfd(paths):
    """
    List files and directories.

    Lists all files and directories in the current directory or specified paths.

    Arguments:
        paths (tuple of Path): Paths to list. If no paths are provided, lists the contents of the current directory.

    Examples:
        flio lfd
        flio lfd /path/to/directory
    """
    if len(paths) == 0:
        click.echo("\t")

        for entry in Path.cwd().iterdir():
            file = click.style(f"   FILE - {entry.name}", fg="cyan")
            folder = click.style(f"   DIR - [{entry.name}]", fg="green")
            click.echo(folder if entry.is_dir() else file, nl=True, color=True)

        return

    for i, path in enumerate(paths):
        click.echo("\t")

        if len(paths) > 1:
            click.echo(f"({path}):")

        for entry in path.iterdir():
            file = click.style(f"   FILE - {entry.name}", fg="cyan")
            folder = click.style(f"   DIR - [{entry.name}]", fg="green")
            click.echo(folder if entry.is_dir() else file, nl=True, color=True)

        if i > 1:
            click.echo("\t")


@cli.command(help="Create directories and sub-directories.")
@click.argument("path", nargs=-1, type=click.Path(file_okay=False, exists=False, path_type=Path))
def crd(path):
    """
    Create directories.

    Creates one or more directories.

    Arguments:
        path (tuple of Path): Paths to directories to be created. If directories already exist, they are not modified.

    Examples:
        flio crd new_directory another_directory
    """
    if len(path) == 0:
        click.echo("No path was given.")
        return

    for i, p in enumerate(path):
        p.mkdir(parents=True, exist_ok=True)

    click.echo(click.style(f"\n-> ({len(path)}) directory(s) have been created.", fg="green"))


@cli.command(help="Create files in the current (or a given) path.")
@click.option(
    "-p", "--path", nargs=1, type=click.Path(exists=False, path_type=Path), help="Custom path where the file(s) will be saved."
)
@click.argument("filename", nargs=-1, type=click.File(mode="w", encoding="utf-8"))
def crf(filename, path):
    """
    Create files.

    Creates one or more files in the current directory or specified path.

    Arguments:
        filename (tuple of File): Names of files to be created.
        path (Path, optional): Custom path where the files will be created. If not provided, files are created in the current directory.

    Examples:
        flio crf file1.txt file2.txt
        flio crf file1.txt file2.txt -p /path/to/directory
    """
    if path:
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)

        for f in filename:
            with open(path / f.name, "w") as file:
                file.write("")

        click.echo(f"\n-> ({len(filename)}) file(s) have been created.")
        return

    if len(filename) == 0:
        click.echo("No file was given.")
        return

    for f in filename:
        with open(f.name, "w") as file:
            file.write("")

    click.echo(click.style(f"\n-> ({len(filename)}) file(s) have been created.", fg="cyan"))


@cli.command(help="Purge files and folders.")
@click.argument("paths", nargs=-1, type=click.Path(exists=True, file_okay=True, readable=True, path_type=Path))
def prg(paths):
    """
    Purge files and directories.

    Deletes specified files and directories. Requires user confirmation.

    Arguments:
        paths (tuple of Path): Paths of files and directories to be deleted.

    Examples:
        flio prg file1.txt directory1
    """
    if len(paths) < 1:
        click.echo("No files or directories were selected.")
        return

    click.echo("\t")

    if not click.confirm("Affirmative?", abort=True):
        sys.exit(1)

    click.echo("\t")

    dirs = []
    files = []

    for i, path in enumerate(paths):

        # Directories
        if path.is_dir():
            delete_folder(path)
            dirs.append(i)

        # Files
        if path.is_file():
            path.unlink(path)
            files.append(i)

    if len(dirs) > 0:
        click.echo(click.style(f"-> ({len(dirs)}) directory(s) have been removed.", fg="green"))

    if len(files) > 0:
        click.echo(click.style(f"-> ({len(files)}) file(s) have been removed.", fg="cyan"))


@cli.command(help="Show the content of one or more files.")
@click.argument("files", nargs=-1, type=click.File(mode="r"))
def cnt(files):
    """
    Show file contents.

    Displays the content of one or more files.

    Arguments:
        files (tuple of File): Files to display the contents of.

    Examples:
        flio cnt file1.txt file2.txt
    """
    if len(files) > 0:
        click.echo("\t")
        for file in files:
            click.echo(f"-> {file.name}")
            click.echo("...................", nl=True)
            click.echo("", nl=True)
            click.echo(f"{file.read().rstrip()}")
            click.echo("...................", nl=True)
            click.echo("\t", nl=True)
    else:
        click.echo("No file was given.")


cli.add_command(lfd)
cli.add_command(crd)
cli.add_command(crf)
cli.add_command(cnt)
cli.add_command(prg)


if __name__ == "__main__":
    cli()
