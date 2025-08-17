from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('Requirements.txt not found') 
        return requirement_lst
    
    return requirement_lst   


print(get_requirements())




setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ganesh",
    author_email="lunavathganesh@gmail.com",
    packages=find_packages(),
    intall_requirements=get_requirements()
)