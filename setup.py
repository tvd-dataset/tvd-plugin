#!/usr/bin/env python
# encoding: utf-8

#
# The MIT License (MIT)
#
# Copyright (c) 2013-2014 Hervé BREDIN (http://herve.niderb.fr/)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

# --- UPDATE THIS SECTION AS REQUIRED ---

# Name of your TV series pluing in CamelCase
# e.g. GameOfThrones, TheBigBangTheory, SixFeetUnder
SERIES_NAME = 'SeriesName'
# This will become the name of your plugin class:
# >>> from tvd.series import GameOfThrones
# This should also be the name of the directory
# containing __init__.py and tvd.yml

# Plugin author name and email address
AUTHOR_NAME = 'John Doe'
AUTHOR_EMAIL = 'john@doe.com'

# TVD compatibility version
REQUIRES_TVD = 'tvd>=0.2.1'

# Additional package dependency
# e.g. ['beautifulsoup4>=4.3.2', 'requests>2.2.1']
REQUIRES_OTHER = []

# --- DO NOT MODIFY ANYTHING AFTER THIS LINE ---
# --- UNLESS YOU KNOW WHAT YOU ARE DOING :-) ---

import versioneer
versioneer.versionfile_source = '{name}/_version.py'.format(name=SERIES_NAME)
versioneer.versionfile_build = '{name}/_version.py'.format(name=SERIES_NAME)
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = '{name}-'.format(name=SERIES_NAME)

try:
    from ez_setup import use_setuptools
    use_setuptools()
except:
    pass

from setuptools import setup, find_packages

setup(
    name='TVD{name}'.format(name=SERIES_NAME),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="{name} plugin for TVD dataset".format(name=SERIES_NAME),
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    package_data={
        SERIES_NAME: ['tvd.yml']
    },
    include_package_data=True,
    install_requires=[REQUIRES_TVD] + REQUIRES_OTHER,
    entry_points="""
        [tvd.series]
        {name}={name}:{name}
    """.format(name=SERIES_NAME)
)
