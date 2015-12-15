# Copyright (c) 2015 CGI
# Contains code Copyright 2009 Asa Wilson

from setuptools import setup

setup(
    name = 'DirtyFormPlugin',
    version = '0.1',
    author = 'Nick Piper',
    author_email = 'nick.piper@cgi.com',
    maintainer="CGI CoreTeam",
    maintainer_email="coreteam.service.desk.se@cgi.com",
    contact="CGI CoreTeam",
    contact_email="coreteam.service.desk.se@cgi.com",
    classifiers=['License :: OSI Approved :: BSD License'],
    license='BSD',
    url='http://define.primeportal.com/',
    description = 'Adds a warning if the user might lose changes to a form.',
    packages = ['dirtyformplugin'],
    package_data = {'dirtyformplugin' : ['htdocs/css/*.css', 'htdocs/js/*.js']}, 
    entry_points = {'trac.plugins': ['dirtyformplugin = dirtyformplugin']},
    install_requires = [''],
)
