from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e.'
def get_requirenments(file_path: str) -> List[str]: 
    requirenments = []
    with open(file_path) as file_obj:
        requirenments = file_obj.readlines()
        requirenments = [req.replace("\n", "") for req in requirenments]
    
    if HYPEN_E_DOT in requirenments:
        requirenments.remove(HYPEN_E_DOT)

    return requirenments

       
setup(
    name ='Fault detection',
    version = '0.0.1',
    author = 'Tanush Lichade',
    author_email = 'tanushlichade@gmail.com',
    install_requirements = get_requirenments('requirenments.txt'),
    packages = find_packages()
)