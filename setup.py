#!/usr/bin/env python
import sys
from setuptools import setup

module_name = 'pflow'

# Dependencies
install_requires = [
    'argparse',
    'networkx',  # writing graphml files
    'gevent',
    #'haigha',  # amqp
    'pyparsing',  # fbp grammar
    'gevent-websocket',  # fbp network runtime
    'python-coveralls',  # code coverage

    # Component-specific stuff
    'requests',
    'sh',
    'pymongo'
]

# Test dependencies
test_requires = [
]


# Dependencies: Python 3.x backports for 2.x
if sys.version_info.major < 3:
    install_requires.append('enum34')  # enum.Enum
    test_requires.append('mock')  # mock (now in unittest.mock)

# Sets __version__
execfile('%s/version.py' % module_name)

setup(
    name=module_name,
    version=__version__,

    author='Chris Lyon',
    author_email='chrisl@luma-pictures.com',

    description='%s - Flow Based Programming for Python' % module_name,
    long_description=open('README.md').read(),

    url='https://github.com/Flushot/%s' % module_name,

    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers'
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
    ],

    install_requires=install_requires,

    test_suite=module_name,
    tests_require=test_requires
)
