from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='keelib',
    version='0.1.1',
    description='KEE by Jaegerwald, but as a library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Zoid',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'colorama'
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
