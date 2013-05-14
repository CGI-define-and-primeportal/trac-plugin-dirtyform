# Copyright (c) 2010, Logica
# Contains code Copyright 2009 Asa Wilson

from setuptools import setup

setup(
    name = 'DirtyFormPlugin',
    version = '0.1',
    author = 'Nick Piper',
    author_email = 'nick.piper@logica.com',
    description = 'Adds a warning if the user might lose changes to a form.',
    license =  """Copyright (c) 2010, Logica. Released under the MIT license. """,
    url = "http://define4.trac.uk.logica.com",
    packages = ['dirtyformplugin'],
    package_data = {'dirtyformplugin' : ['htdocs/css/*.css', 'htdocs/js/*.js']}, 
    entry_points = {'trac.plugins': ['dirtyformplugin = dirtyformplugin']},
    install_requires = [''],
)
