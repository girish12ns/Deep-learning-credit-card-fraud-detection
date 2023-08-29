from setuptools import setup,find_packages
import os

with open('README.md','r') as f:
    long_des=f.read()

project_repo='Artifical Neural Network'
src_repo='card_fraud_dection'

_version_='0.0.0'
Author_id='girish12n'

setup(
    version=_version_,
    name=project_repo,
    long_description=long_des,
    author=Author_id,
    author_email='girish12n@gmail.com',
    url="https://github.com/{Author_id}/{project_repo}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_id}/{project_repo}/issues",
    },

    package_dir={"":"src"},
    packages=find_packages(where="src"))






