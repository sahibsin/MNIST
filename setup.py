

# setup.py
from setuptools import setup, find_packages

setup(name='example5',
        version='0.1',
        packages=find_packages(),
        description='example to run keras on gcloud ml-engine',
        author='Sahib Singh',
        author_email='sahib.chelsea@gmail.com',
        install_requires=[
                  'keras',
                  'h5py'
              ],
        zip_safe=False)