from __future__ import unicode_literals

import os, pytest

from pre_commit_hooks.rst_linter import get_linter_error


@pytest.mark.parametrize(
    ('test_file_path', 'expected'),
    (
        ('README_1.rst', '<string>:2: (WARNING/2) Title underline too short.\n\nABCDE\n====\n'),
    ),
)
def test_get_linter_errors(test_file_path, expected):
    assert get_linter_error(os.path.join('tests', 'resources', test_file_path)) == expected
