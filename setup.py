from setuptools import setup, find_packages

setup(
    name='epiasapi',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    description='Epiaş Rest Services API',
    url='https://github.com/metehanboy/epiasapi',
    author='metehanboy',
    author_email='m3t3-han@hotmail.com',
    license='GNUv3'
)