# -*- coding: utf-8 -*-
#
# Copyright © 2013 The Spyder Development Team
# Licensed under the terms of the MIT License
# (see spyderlib/__init__.py for details)

"""
IPython configuration variables needed by Spyder
"""

from spyderlib.utils import programs


def is_qtconsole_installed():
    pyzmq_installed = programs.is_module_installed('zmq')
    pygments_installed = programs.is_module_installed('pygments')
    ipyqt_installed = programs.is_module_installed('IPython.qt')
    ipy4_installed = programs.is_module_installed('IPython', '>=4.0')

    if ipyqt_installed and pyzmq_installed and pygments_installed:
        if ipy4_installed:
            if programs.is_module_installed('qtconsole'):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


SUPPORTED_IPYTHON = '>=1.0'
IPYTHON_QT_INSTALLED = is_qtconsole_installed()
