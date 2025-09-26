from __future__ import unicode_literals

from os import path

import pytest

from pre_commit_hooks.rst_linter import get_linter_error


@pytest.mark.parametrize(
    ('test_file_path', 'expected'),
    (
        ('README_1.rst', '<string>:2: (WARNING/2) Title underline too short.\n\nABCDE\n====\n'),
        ('README_with_raw_html.rst', '<string>:4: (WARNING/2) "raw" directive disabled.\n'),
    ),
)
def test_get_linter_errors(test_file_path, expected):
    assert get_linter_error(path.join('tests', 'resources', test_file_path)) == expected


def test_allow_raw():
    assert get_linter_error(path.join('tests', 'resources', 'README_with_raw_html.rst'), allow_raw=True) is False
