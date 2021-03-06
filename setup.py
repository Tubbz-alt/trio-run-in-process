#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)


extras_require = {
    'test': [
        "pytest==5.1.2",
        "pytest-trio==0.5.2",
        "pytest-xdist==1.29.0",
        "tox>=2.9.1,<3",
    ],
    'lint': [
        "black==19.3b0",
        "flake8==3.4.1",
        "isort>=4.2.15,<5",
        "mypy==0.720",
        "pydocstyle>=3.0.0,<4",
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +  # noqa: W504
    extras_require['test'] +  # noqa: W504
    extras_require['lint'] +  # noqa: W504
    extras_require['doc']
)


with open('./README.md') as readme:
    long_description = readme.read()


setup(
    name='trio-run-in-process',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='0.1.0-alpha.1',
    description="""trio-run-in-process: Trio based API for running code in a separate process""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='The Ethereum Foundation',
    author_email='snakecharmers@ethereum.org',
    url='https://github.com/ethereum/trio-run-in-process',
    include_package_data=True,
    install_requires=[
        "async-generator>=1.10,<2",
        "cloudpickle>=1.2.1,<2",
        "trio>=0.12.1,<0.13",
        "trio-typing>=0.2.0,<0.3.0",
    ],
    python_requires='>=3.6, <4',
    extras_require=extras_require,
    py_modules=['trio_run_in_process'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
