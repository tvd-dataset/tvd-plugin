#!/usr/bin/env python
# encoding: utf-8

#
# The MIT License (MIT)
#
# Copyright (c) 2013-2014 CNRS (http://www.cnrs.fr)
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

from tvd.series.plugin import SeriesPlugin
from tvd.common.graph import T


# RENAME SeriesName TO THE NAME YOU DEFINED IN SETUP.PY
# The class will automatically inherit from all SeriesPlugin methods.

class SeriesName(SeriesPlugin):

    # ADD ONE METHOD PER RESOURCE DEFINED IN TVD.YML

    # These methods are called in SeriesPlugin.get_resource()
    # with parameters `episode` and `content`:
    #    - `episode` (Episode) is the currently processed episode
    #    - `content` (str) contains the downloaded content
    #      from the URL provided in tvd.yml. It is pre-downloaded for you.

    # They should return the resource for the given episode
    # as an annotation graph (tvd.AnnotationGraph)
    def firstResource(self, content=None, episode=None):
        """Download `episode` `firstResource` from `url`

        Parameters
        ----------
        content : str
            Downloaded content from the URL provided in file tvd.yml.
        episode : `tvd.Episode`
            Episode

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
