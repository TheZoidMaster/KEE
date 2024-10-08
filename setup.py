from setuptools import setup, find_packages

setup(
    name='keelib',
    version='0.1.0',
    description='KEE by Jaegerwald, but as a library.',
    author='Zoid',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'colorama'
    ]
)
