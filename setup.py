from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str)->List[str]:
    """This function is used to give list of Requirements"""


    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("/n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements






setup(  
name = "Ml_Project",    
version = '0.0.1',
author= "Syed",
author_email = 'sksyedroshan@gmail.com',
packages = find_packages(),
install = get_requirement('requirements.txt')

)

""" git commit -m "First commit"
 git config --global user.email "EMAIL"
 git config --global user.name Rose776
 git push -u origin main"""