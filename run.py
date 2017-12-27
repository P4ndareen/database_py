#!/usr/bin/python3

''' Establishing connection to database '''

from database_py.core import Getter


with Getter('test', 'test').credentials() as start:
    start