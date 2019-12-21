# -*- coding: utf-8 -*-
# flake8: NOQA
"""API for interfacing with tmux servers, sessions, windows and panes.

libtmux
~~~~~~~

:copyright: Copyright 2016-2018 Tony Narlock.
:license: MIT, see LICENSE for details

"""

from .__about__ import (
    __author__,
    __copyright__,
    __description__,
    __email__,
    __license__,
    __package_name__,
    __title__,
    __version__,
)
from .pane import Pane
from .server import Server
from .session import Session
from .window import Window
