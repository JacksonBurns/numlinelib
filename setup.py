import pathlib
from setuptools import setup, find_packages

cwd = pathlib.Path(__file__).parent

README = (cwd / "README.md").read_text()

desc = "Plot number lines in Python"

setup(
    name="numlinelib",
    version="0.0.1",
    description=desc,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JacksonBurns/numlinelib",
    author="Jackson Burns, Kristina Holsapple",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=["matplotlib"],
    packages=["numlinelib"],
)
