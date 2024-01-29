from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'A Python library for Creole text preprocessing'
LONG_DESCRIPTION = 'A Python library designed for preprocessing Creole text. The library includes various functions and tools to clean, tokenize, and prepare text data for natural language processing (NLP) tasks. Dependencies include BeautifulSoup4 and NLTK.'

setup(
    name='creolenltk',
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4>=4.9.3',
        'nltk>=3.6.2',
    ],
    author='John Clayton',
    author_email='jclaytonblanc@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='https://github.com/jcblanc2/CreoleNLTK.git',
    keywords=['python', 'nlp', 'creole', 'natural language processing', 'text preprocessing'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license_files=('LICENSE',),
)