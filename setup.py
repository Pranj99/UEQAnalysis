# setup.py
from setuptools import setup, find_packages

setup(
    name="UEQanalyzer",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for analyzing User Experience Questionnaire (UEQ) data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/UEQanalyzer",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",  # For reading Excel files
        "matplotlib",
    ],
    python_requires=">=3.6",
)