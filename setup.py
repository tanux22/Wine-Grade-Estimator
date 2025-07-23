from setuptools import setup, find_packages

def get_requirements(file_path):
    """
    This function reads the requirements from a file and returns them as a list.
    """
    with open(file_path, "r") as file:
        requirements= file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
    
    
setup(
    name="Wine-Grade-Estimator",
    version="0.0.1",
    author="Tanush Reddy",
    author_email="atanushreddy@gmail.com",
    description="A machine learning project to estimate the grade of wine based on its features.",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)