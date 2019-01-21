
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='neural-activity-resource',
    version='0.1.0',
    description='Python API for the Human Brain Project Neural Activity Resource',
    long_description=long_description,
    url='https://github.com/HumanBrainProject/neural-activity-resource',
    author='Andrew P. Davison',
    author_email='andrew.davison@unic.cnrs-gif.fr',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='nar hbp metadata electrophysiology nexus shacl',
    packages=find_packages(),
    #install_requires=['pyxus']
)
