# from setuptools import find_packages,setup
# from typing import List

# HYPEN_E_DOT='-e .'
# def get_requients(file_path:str)->List[str]:
#     ''''
#     This function return the list of requirements
#     '''
    
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]
        
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
        
#         return requirements
        
#     setup(
#     name="mlproject",
#     version="0.0.1",
#     auther="shadab",
#     auther_email="shadab@tamarsoftware.in",
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
        
#     )
# from setuptools import setup, find_packages
# from typing import List
# HYPEN_E_DOT = "-e ."
from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path) as file:
        return [req.strip() for req in file if req.strip() and req.strip() != '-e .']

setup(
    name="data_science_project",
    version="0.0.1",
    author="shadab",
    author_email="shadab@tamarsoftware.in",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
