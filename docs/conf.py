# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- Project information -----------------------------------------------------
#

project = "kblog"
copyright = "2022, Kai Norman Clasen"
author = "Kai Norman Clasen"

#
# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # External stuff
    "myst_parser",
    "sphinx_external_toc",
    # "sphinx_copybutton",
    # "sphinx_inline_tabs",
]
templates_path = ["_templates"]
external_toc_path = "_toc.yml"

#
# -- Options for extlinks ----------------------------------------------------
#
extlinks = {
    "pypi": ("https://pypi.org/project/%s/", ""),
}

#
# -- Options for intersphinx -------------------------------------------------
#
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

#
# -- Options for TODOs -------------------------------------------------------
#
# todo_include_todos = True

#
# -- Options for Markdown files ----------------------------------------------
#
myst_enable_extensions = [
    "deflist",
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
# myst_title_to_header = True
# myst_heading_anchors = 2
# myst_heading_anchors = 3

#
# -- Options for HTML output -------------------------------------------------
#

html_theme = "kblog"
html_title = "kblog"
