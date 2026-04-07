import os
from setuptools import setup, find_packages

version_dict = {}
version_path = os.path.join(os.path.dirname(__file__), 'ampliclip', 'version.py')
with open(version_path, 'r') as f:
    exec(f.read(), version_dict)

setup(
    name='ampliclip',
    version=version_dict['__version__'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ampliclip=ampliclip.ampliclip:main',
        ]
    },
    install_requires=[
        'biopython>=1.70',
        'pysam>=0.20'
    ],
    description='Tool to softclip reads in bam files based on amplicon primers',
    url='https://github.com/dnieuw/ampliclip',
    author='David F. Nieuwenhuijse',
    author_email='d.nieuwenhuijse@erasmusmc.nl',
    license='BSD 3-Clause',
    zip_safe=False
)
