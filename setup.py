from setuptools import find_packages,setup # type: ignore

from typing import List


def get_requirements()->List[str]:

    reqirements_list : List[str] = []

    return reqirements_list


 
setup(
    name ='sensor',
    version = "0.0.1",
    author = "vishal",
    author_email = "vishaltiwaribnt@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(), #["pymongo"]

)