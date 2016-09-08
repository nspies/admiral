from setuptools import setup, find_packages

setup(
    name = 'admiral',
    version = '0.1dev0',

    author = "Noah Spies",
    url = "https://github.com/nspies/admiral",
    
    packages = find_packages('src'),
    package_dir = {"": "src"},

    install_requires = ["humanfriendly"]

)
