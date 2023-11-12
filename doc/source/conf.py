# Configuration file for the Sphinx documentation builder.

import os
import sys

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "mpl_bsic"
copyright = "2023, Andrea Franceschini"
author = "Andrea Franceschini"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

package_path = os.path.abspath("../../mpl_bsic")
sys.path.insert(0, package_path)
print(package_path)
print(os.listdir(package_path))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "numpydoc",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.imgmath",
    "nbsphinx",
    "sphinx_simplepdf",
    "matplotlib.sphinxext.plot_directive",
]

templates_path = ["_templates"]
exclude_patterns = []

autosummary_generate = True

# -- Options for NumpyDocs  ---------------------------------------------
numpydoc_xref_param_type = True
numpydoc_xref_ignore = {"optional", "type_without_description", "BadException"}
numpydoc_class_members_toctree = True
numpydoc_validation_checks = {"all", "GL01", "GL02", "SA04", "RT03"}
pygments_style = "sphinx"

# -- Options for matplotlib plots -----------------------------------------
plot_include_source = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

# -- Intersphinx setup ----------------------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/devdocs/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
}
