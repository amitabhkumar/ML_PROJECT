# This script will be responsible in creating the Machine Learning Application as a Package, and even Deploy in the Python Pypy from where andone can install and use it.
# We can install this Package in any Projects, with the help of setup.py
# It basically holds the meta-data of the Package.

from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    """This function will return the list of requirements."""
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements




setup(
    name = 'ML_PROJECT',
    version = '0.0.1',
    author = 'Rahul',
    author_email = 'amitabh.kumar467@yahoo.com',
    packages = find_packages(),
    ####install_requires = ['pandas', 'numpy', 'seaborn']
    ### We can directly install all the requirements or whenever we're trying to install 
    ### the requirements.txt, at that point of time setup.py should also run to build the Packages. 
    ### To enable that, we need to specify '-e .' at the last line in requirements.txt file, to Trigget setup.py.
    ### While reading the get_requirements function '-e .y' will also come, and
    ### while installing get_requirements in the form of List '-e .' will also come and it should get connected to setup.py. But '-e .' should not come here when we're actually running the code.
    install_requires = get_requirements('requirements.txt')


)