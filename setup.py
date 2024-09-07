from setuptools import setup, find_packages


setup(
    name="fdio",
    version="1.0.0",
    description="A CLI tool that manages files and directories.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ayoub A.",
    author_email="aberbach.me@gmail.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        'importlib-metadata; python_version < "3.11"',
    ],
    entry_points={
        "console_scripts": [
            "executable-name = fdio.fdio:cli",
        ],
    },
    url="https://github.com/ayoub-aberbach/fdio",
)
