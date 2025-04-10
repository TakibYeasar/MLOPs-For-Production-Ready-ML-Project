from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
SRC_REPO = "MLOps For Production Ready ML Projects..."
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.0",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    author="Yeasar",
    author_email="mdtakibyeasar@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)