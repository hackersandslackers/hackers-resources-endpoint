"""Report setup."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Jira Resources Endpoint',
    version='0.0.1',
    description='Pulls Jira issues for building kanban board.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/hackers-resources-endpoint',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Database SQLAlchemy Postgres',
    packages=find_packages(),
    install_requires=['SQLAlchemy', 'Psycopg2-Binary', 'SimpleJSON'],
    entry_points={
        'console_scripts': [
            'main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/hackers-resources-endpoint/issues',
        'Source': 'https://github.com/hackersandslackers/hackers-resources-endpoint/',
    },
)
