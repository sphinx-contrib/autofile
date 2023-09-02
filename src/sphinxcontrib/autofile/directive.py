r"""Directive
=============
"""
import os
from glob import glob

from docutils import nodes
from docutils.nodes import Node
from docutils.statemachine import StringList
from jinja2 import Template
from myst_parser.mdit_to_docutils.sphinx_ import SphinxRenderer
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import nested_parse_with_titles

TEMPLATE_DIR = os.path.join(
    os.path.join(os.path.dirname(__file__), "assets"), "jinja2"
)
OPTION_SPEC = {
    "members": str,
    "undoc-members": str,
    "private-members": str,
    "special-members": str,
}


class AutofileDirective(SphinxDirective):
    r"""Autofiledirective."""

    has_content = True
    option_spec = OPTION_SPEC | {
        "prefix": str,
        "template": str,
    }

    def run(self) -> list[Node]:
        r"""Run.

        :rtype: list[Node]
        """
        if isinstance(self.state._renderer, SphinxRenderer):
            template_ext = "md"
        else:
            template_ext = "rst"
        template = self.options.get("template")
        if template is None:
            template = os.path.join(
                TEMPLATE_DIR, f"template.{template_ext}.j2"
            )
        with open(template) as f:
            template_text = f.read()

        prefix = self.options.get("prefix", self.config["autofile_prefix"])
        path = self.content.items[0][0]
        items = []
        for expr in self.content.data:
            expr = os.path.abspath(os.path.join(os.path.dirname(path), expr))
            for abspath in glob(expr, recursive=True):
                _, _, module_path = abspath.rpartition("/" + prefix + "/")
                module_name = (
                    module_path.replace("/__init__.py", "")
                    .replace(".py", "")
                    .replace("/", ".")
                )
                items += [module_name]
        data = {}
        for opt in OPTION_SPEC:
            val = self.options.get(opt)
            if val is None:
                continue
            if val == "None":
                val = ""
            data[opt] = val
        final_content = Template(template_text).render(items=items, data=data)
        string_list = StringList(final_content.splitlines(), source="")
        node = nodes.Element()
        nested_parse_with_titles(self.state, string_list, node)

        return node.children
