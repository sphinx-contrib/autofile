r"""Sphinx extension: autofile
==============================
"""
from sphinx.application import Sphinx

from ._version import __version__, __version_tuple__  # type: ignore
from .directive import AutofileDirective


def setup(app: Sphinx) -> None:
    r"""Set up.

    :param app:
    :type app: Sphinx
    :rtype: None
    """
    app.add_config_value(name="autofile_prefix", default="src", rebuild="env")
    app.add_directive(name="autofile", cls=AutofileDirective)
