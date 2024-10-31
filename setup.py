
from setuptools import setup, find_packages

setup(
    name='submission',
    version='1.0.0',
    packages=find_packages(),
    author='Patrick Chen',
    author_email='patrickechohelloworld@outlook.com',
    description='A python package for kelvinlby/submission',
    url='https://github.com/ECHO-HELLO-WORLD424/submission_client',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    install_requires=[
        'grpcio',
        'grpcio-tools',
    ]
)
