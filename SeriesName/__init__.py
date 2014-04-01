#!/usr/bin/env python
# encoding: utf-8

#
# The MIT License (MIT)
#
# Copyright (c) 2013-2014 CNRS (Hervé BREDIN - http://herve.niderb.fr/)
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

from tvd import Plugin
from tvd import TFloating, TStart, TEnd, AnnotationGraph

# RENAME SeriesName TO THE NAME YOU DEFINED IN SETUP.PY
# The class will automatically inherit of all Plugin methods.

class SeriesName(Plugin):

    # ADD ONE METHOD PER RESOURCE DEFINED IN TVD.YML

    # These methods are called in Plugin.get_resource()
    # with parameters `episode` and `url`:
    #    - `episode` (Episode) is the currently processed episode
    #    - `url` (str) provided in tvd.yml. 

    # They should return the resource for the given episode
    # as an annotation graph (tvd.AnnotationGraph)
    def firstResource(self, url=None, episode=None, **kwargs):
        """Download `episode` `firstResource` from `url`

        Parameters
        ----------
        url : str, optional
            URL provided in file tvd.yml.
        episode : `tvd.Episode`, optional
            Episode for which resource should be downloaded.
            Useful in case a same URL contains resources for multiple episodes.
        Returns
        -------
        graph : `tvd.AnnotationGraph`
        """
        pass

    def secondResource(self, content=None, episode=None):
        pass

# --- DO NOT MODIFY ANYTHING AFTER THIS LINE ---
# --- UNLESS YOU KNOW WHAT YOU ARE DOING :-) ---

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
