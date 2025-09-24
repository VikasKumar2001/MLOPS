from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()  # remove spaces, newlines
            if req and req != HYPEN_E_DOT:  # skip blanks and '-e .'
                requirements.append(req)
    return requirements   

setup(
    name='mlproject',
    version='0.0.1',
    author='Vikas',
    author_email='kvikas1482@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)