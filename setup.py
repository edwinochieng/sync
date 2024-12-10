from setuptools import setup, find_packages

setup(
    name="sync",
    version="0.1",
    py_modules=["main"],  
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sync=main:main",  
        ],
    },
)
