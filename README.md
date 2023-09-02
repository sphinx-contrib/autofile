# sphinxcontrib-autofile

[![readthedocs](https://shields.io/readthedocs/sphinxcontrib-autofile)](https://sphinx-contrib-autofile.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sphinx-contrib/autofile/main.svg)](https://results.pre-commit.ci/latest/github/sphinx-contrib/autofile/main)
[![github/workflow](https://github.com/sphinx-contrib/autofile/actions/workflows/main.yml/badge.svg)](https://github.com/sphinx-contrib/autofile/actions)
[![codecov](https://codecov.io/gh/sphinx-contrib/autofile/branch/main/graph/badge.svg)](https://codecov.io/gh/sphinx-contrib/autofile)

[![github/downloads](https://shields.io/github/downloads/sphinx-contrib/autofile/total)](https://github.com/sphinx-contrib/autofile/releases)
[![github/downloads/latest](https://shields.io/github/downloads/sphinx-contrib/autofile/latest/total)](https://github.com/sphinx-contrib/autofile/releases/latest)
[![github/issues](https://shields.io/github/issues/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/discussions)
[![github/milestones](https://shields.io/github/milestones/all/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/milestones)
[![github/forks](https://shields.io/github/forks/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/network/members)
[![github/stars](https://shields.io/github/stars/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/stargazers)
[![github/watchers](https://shields.io/github/watchers/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/watchers)
[![github/contributors](https://shields.io/github/contributors/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/commits)
[![github/release-date](https://shields.io/github/release-date/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/releases/latest)

[![github/license](https://shields.io/github/license/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile)
[![github/languages/top](https://shields.io/github/languages/top/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile)
[![github/directory-file-count](https://shields.io/github/directory-file-count/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile)
[![github/code-size](https://shields.io/github/languages/code-size/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile)
[![github/repo-size](https://shields.io/github/repo-size/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile)
[![github/v](https://shields.io/github/v/release/sphinx-contrib/autofile)](https://github.com/sphinx-contrib/autofile)

[![pypi/status](https://shields.io/pypi/status/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-autofile/#description)
[![pypi/v](https://shields.io/pypi/v/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-autofile/#history)
[![pypi/downloads](https://shields.io/pypi/dd/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-autofile/#files)
[![pypi/format](https://shields.io/pypi/format/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-autofile/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-autofile/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/sphinxcontrib-autofile)](https://pypi.org/project/sphinxcontrib-autofile/#files)

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
[![readthedocs](https://shields.io/readthedocs/sphinxcontrib-autofile)](https://sphinxcontrib-autofile.readthedocs.io)
to know more.
