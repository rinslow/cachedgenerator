"""Setup file for handling packaging and distribution."""
from setuptools import setup

setup(
    name='cachedgenerator',
    packages=['cachedgenerator'],
    version='0.1.0',
    description='Caching generators has never been prettier.',
    author='Dan Elkis',
    author_email='elkissdan@gmail.com',
    license='MIT',
    zip_safe=False,
    url='https://github.com/rinslow/cachedgenerator',
    keywords=['cached', 'cache', 'caching', 'generator', 'generators', 'cachedgenerator', 'cached_generator'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
