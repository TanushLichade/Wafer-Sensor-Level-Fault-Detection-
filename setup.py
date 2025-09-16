from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]: 
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # remove \n and spaces
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='FaultDetection',
    version='0.0.1',
    author='Tanush Lichade',
    author_email='tanushlichade@gmail.com',
    install_requires=get_requirements('requirements.txt'),  # fixed
    packages=find_packages()
)
