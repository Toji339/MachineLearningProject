from setuptools import find_packages,setup
"""
#with the help of setup.py, we will be build the entire machine learning application 
as a package and we can deploy in py , so everyone can download and use it.
"""
setup(
    name = "MachineLearningProject",
    version='0.0.1',
    author = "Venkata Dharaneswara Reddy",
    author_email="dharaneswar339@gmail.com",
    packages=find_packages(),
    install_requires = ['numpy','pandas','seaborn']
)