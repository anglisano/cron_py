import os
import fnmatch

from typing import List
from setuptools import (
    find_packages,
    setup
)

from cron_py._version import __version__

PKG_ROOT = os.path.dirname((os.path.abspath(__file__)))


def get_requirements() -> List[str]:
    with open(os.path.join(PKG_ROOT, 'requirements.txt')) as f:
        req = filter(lambda x: x != '', [
                     x for x in f.read().splitlines() if '#' not in x])
    return list(req)


def get_package_data_files(pattern: str) -> List[str]:

    path = os.path.join(PKG_ROOT, 'cron_py')

    if isinstance(pattern, str):
        pattern = [pattern]

    file_has_pattern = lambda file, wildcard: fnmatch.fnmatch(file, wildcard)

    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if any([file_has_pattern(name, pat) for pat in pattern]):
                result.append(os.path.join(root, name))
    return result

setup(
    name='cron_py',
    version=__version__,
    description='cron tab handler',
    author='Marc anglisano',
    author_email='marcanglisano@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(
        include=["cron_py.*", "cron_py"]
    ),
    package_data={
        'cron_py': [
            *get_package_data_files(pattern='*.yml'),
            *get_package_data_files(pattern='*.html'),
            *get_package_data_files(pattern='*.txt'),
        ]
    },
    python_requires='>=3.8',
    license='',
)