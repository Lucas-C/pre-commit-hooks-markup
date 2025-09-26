from __future__ import print_function

import argparse, sys
from io import StringIO

from readme_renderer.rst import publish_parts, ReadMeHTMLTranslator, SETTINGS, SystemMessage, Writer


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    parser.add_argument('-r', '--allow-raw', action='store_true', help='Allow the "raw" directive')
    args = parser.parse_args(argv)

    errors_found = False
    for filename in args.filenames:
        linter_error = get_linter_error(filename, args.allow_raw)
        if linter_error:
            errors_found = True
            print('Syntax error found in ', filename, file=sys.stderr)
            print(linter_error, file=sys.stderr)

    return 1 if errors_found else 0


def get_linter_error(filename, allow_raw=False):
    output = StringIO()

    settings = SETTINGS.copy()
    settings['warning_stream'] = output
    settings['raw_enabled'] = allow_raw

    writer = Writer()
    writer.translator_class = ReadMeHTMLTranslator

    with open(filename, encoding="utf8") as rst_content:
        raw = rst_content.read()

    try:
        publish_parts(raw, writer=writer, settings_overrides=settings).get('fragment')
        return False
    except SystemMessage:
        return output.getvalue()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
