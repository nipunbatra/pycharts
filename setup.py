from distutils.core import setup
import warnings
import setuptools
setup(
    name='pycharts',
    version='0.0.1',
    author='ABCD',
    author_email='nipun',
    packages=['pycharts'],
    scripts=[],
    url='https://github.com/nipunreddevil/pycharts',
    license='',
    description='pycharts',
    install_requires=[
        'numpy>=1.7', 'pandas>=0.12', 'plotly'
    ],
)
