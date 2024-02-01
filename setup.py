from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.1.3'
DESCRIPTION = 'A Python library for Creole text preprocessing'
LONG_DESCRIPTION = (Path(__file__).parent / "README.md").read_text()

setup(
    name='creolenltk',
    version=VERSION,
    packages=find_packages(exclude=('test*',)),
    install_requires=[
        'beautifulsoup4>=4.9.3',
        'nltk>=3.6.2',
    ],
    author='John Clayton',
    author_email='jclaytonblanc@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/jcblanc2/CreoleNLTK.git',
    keywords=['python', 'nlp', 'creole', 'natural language processing', 'text preprocessing'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license_files=('LICENSE',),
)
