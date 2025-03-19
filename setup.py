# setup.py
import os
import re
from setuptools import setup, find_packages

def get_version():
    # Read the version from _version.py
    with open(os.path.join("UEQanalyzer", "_version.py"), "r") as f:
        version_file = f.read()
    version_match = re.search(r'^__version__ = ["\']([^"\']*)["\']', version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name="UEQanalyzer",
    version=get_version(),  # Use the version from _version.py
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "openpyxl",  # Required for reading Excel files
    ],
    entry_points={
        "console_scripts": [
            "ueqanalyzer=cli:main",  # Add this line for the CLI
        ],
    },
)