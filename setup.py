from setuptools import setup, find_packages

setup_config = {
    "name": "beam_helper", 
    "version": "0.0.1",
    "author": "chrisp",
    "author_email": "christopherpearce10@gmail.com",
    "description": "class providing help for apache beam pipeline rapid development",
    "install_requires": ["wheel","apache_beam"],
    "packages": find_packages(where='.', include='*'),
    "include_package_data": True
}

setup(
    **setup_config
)