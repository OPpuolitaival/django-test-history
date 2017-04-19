# coding: utf-8
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-info_screen',
    version='0.1',
    description='Simple storage for your test results',
    author='Olli-Pekka Puolitaival',
    author_email='oopee1@gmail.com',
    url='https://github.com/OPpuolitaival/django-reversion-compare',
    license='MIT',
    long_description=README,
    packages=['test_history'],
    install_requires=[
    ],
    classifiers=[
        'Framework :: Django',
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
    include_package_data=True,
)
