from setuptools import setup, find_packages

setup(
    name='multimers',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'biopython',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'multimers-seq-io=multimers.seq_io:main',
        ],
    },
)
