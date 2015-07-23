import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fp:
    long_description = fp.read()

setup(
    name='klok',
    description="convert times into Dutch words",
    long_description=long_description,
    version='0.0.1',
    author='Wouter Bolsterlee',
    author_email='Wouter Bolsterlee',
    url="https://github.com/wbolster/klok",
    py_modules=['klok'],
    install_requires=['telwoord'],
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
