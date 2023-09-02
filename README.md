# sphinxcontrib-autofile

[![readthedocs](https://shields.io/readthedocs/sphinxcontrib-autofile)](https://sphinx-contrib-requirements-txt.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sphinx-contrib/autofile/main.svg)](https://results.pre-commit.ci/latest/github/sphinx-contrib/requirements-txt/main)
[![github/workflow](https://github.com/sphinx-contrib/autofile/actions/workflows/main.yml/badge.svg)](https://github.com/sphinx-contrib/requirements-txt/actions)
[![codecov](https://codecov.io/gh/sphinx-contrib/autofile/branch/main/graph/badge.svg)](https://codecov.io/gh/sphinx-contrib/requirements-txt)

[![github/downloads](https://shields.io/github/downloads/sphinx-contrib/autofile/total)](https://github.com/sphinx-contrib/requirements-txt/releases)
[![github/downloads/latest](https://shields.io/github/downloads/sphinx-contrib/autofile/latest/total)](https://github.com/sphinx-contrib/requirements-txt/releases/latest)
[![github/issues](https://shields.io/github/issues/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/discussions)
[![github/milestones](https://shields.io/github/milestones/all/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/milestones)
[![github/forks](https://shields.io/github/forks/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/network/members)
[![github/stars](https://shields.io/github/stars/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/stargazers)
[![github/watchers](https://shields.io/github/watchers/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/watchers)
[![github/contributors](https://shields.io/github/contributors/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/commits)
[![github/release-date](https://shields.io/github/release-date/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/releases/latest)

[![github/license](https://shields.io/github/license/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt)
[![github/languages/top](https://shields.io/github/languages/top/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt)
[![github/directory-file-count](https://shields.io/github/directory-file-count/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt)
[![github/code-size](https://shields.io/github/languages/code-size/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt)
[![github/repo-size](https://shields.io/github/repo-size/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt)
[![github/v](https://shields.io/github/v/release/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/requirements-txt)

[![pypi/status](https://shields.io/pypi/status/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-requirements-txt/#description)
[![pypi/v](https://shields.io/pypi/v/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-requirements-txt/#history)
[![pypi/downloads](https://shields.io/pypi/dd/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-requirements-txt/#files)
[![pypi/format](https://shields.io/pypi/format/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-requirements-txt/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-requirements-txt/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-requirements-txt/#files)

A sphinx extension to generate module for many files from a glob expression.

## Usage

Take MyST as an example. rst is similar.

`docs/conf.py`:

```python
# ...
extensions = [
    "myst_parser",
    "sphinxcontrib.autofile",
]
# ...
```

`docs/index.md`:

````markdown
```{autofile} ../src/sphinxcontrib/autofile/*.py
:members:
```
````

It will be translated to

````markdown
```{eval-rst}
.. automodule:: sphinxcontrib.autofile
    :members:

.. automodule:: sphinxcontrib.autofile.directive
    :members:

... (more modules)
```
````

When your modules is too many, it will save your time.

## Customize

````markdown
```{autofile} ../src/sphinxcontrib/autofile/*.py
:prefix: your_prefix
:template: /the/path/of/your/template
```
````

- `prefix`: If you don't use src-layout, change it.
- `template`: template use
  [jinja syntax](https://docs.jinkan.org/docs/jinja2/templates.html).
  See
  [examples](https://github.com/sphinx-contrib/autofile/tree/main/src/sphinxcontrib/autofile/assets/jinja2).

## Alternatives

- [sphinxcontrib-eval](https://github.com/sphinx-contrib/eval#generate-api-document)

See
[![readthedocs](https://shields.io/readthedocs/sphinxcontrib-autofile)](https://sphinxcontrib-requirements-txt.readthedocs.io)
to know more.
