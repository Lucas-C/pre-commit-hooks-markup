[![build status](https://github.com/Lucas-C/pre-commit-hooks-markup/workflows/CI/badge.svg)](https://github.com/Lucas-C/pre-commit-hooks-markup/actions?query=branch%3Amaster)
[![Known Vulnerabilities](https://snyk.io/test/github/lucas-c/pre-commit-hooks-markup/badge.svg)](https://snyk.io/test/github/lucas-c/pre-commit-hooks-markup)

Hooks for [pre-commit](https://pre-commit.com) that validate Markdown / RST files

## Usage

    - repo: https://github.com/Lucas-C/pre-commit-hooks-markup
      rev: v1.0.1
      hooks:
      - id: rst-linter

To enable the `.. raw::` directive, you can add:

      - id: rst-linter
        args: [--allow-raw]

Note that this is a potential security hole, and will prevent rendering of the
`README.rst` file on PyPI.
See [docutils documentation][1] and [Python Packaging User Guide][2]
for more information.

[1]: https://docutils.sourceforge.io/docs/ref/rst/directives.html
[2]: https://packaging.python.org/guides/making-a-pypi-friendly-readme/
