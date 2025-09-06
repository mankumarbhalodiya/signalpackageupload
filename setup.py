from setuptools import setup, find_packages
import os

# Read README.md content
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Python package for signal generation, processing, and visualization."

setup(
    name="signal_ManKumar_125",  # ✅ Make sure this matches your actual folder name
    version="1.0.0",
    author="Man Kumar",
    author_email="mankumar@example.com",  # Update if needed
    description="Python package for signal generation and operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/signal_ManKumar_125",  # Optional: update if you create a repo
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18.0",
        "matplotlib>=3.1.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires='>=3.6',
    include_package_data=True,
)
