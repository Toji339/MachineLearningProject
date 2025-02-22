from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path, "r") as file_obj:
        requirements = file_obj.read().splitlines()
        requirements = [req for req in requirements if req and not req.startswith("-e")]  
        return requirements

setup(
    name="MachineLearningProject",
    version="0.0.1",
    author="Venkata Dharaneswara Reddy",
    author_email="dharaneswar339@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
