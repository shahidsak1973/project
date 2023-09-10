from setuptools import find_packages,setup
from typing import List
HYPEN_E_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_dot in requirements:
            requirements.remove(HYPEN_E_dot)
    return requirements

setup(
    name='Regression',
    author='shahid',
    version='1.0',
    author_email='shaikshahidvali2000@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()


)