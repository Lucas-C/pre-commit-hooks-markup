from __future__ import print_function

import argparse, io, sys

from readme_renderer.rst import publish_parts, ReadMeHTMLTranslator, SETTINGS, SystemMessage, Writer


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    args = parser.parse_args(argv)

    errors_found = False
    for filename in args.filenames:
        linter_error = get_linter_error(filename)
        if linter_error:
            errors_found = True
            print('Syntax error found in ', filename, file=sys.stderr)
            print(linter_error, file=sys.stderr)

    return 1 if errors_found else 0


def get_linter_error(filename):
    output = io.StringIO()

    settings = SETTINGS.copy()
    settings['warning_stream'] = output

    writer = Writer()
    writer.translator_class = ReadMeHTMLTranslator

    with open(filename) as rst_content:
        raw = rst_content.read()

    try:
        publish_parts(raw, writer=writer, settings_overrides=settings).get('fragment')
        return False
    except SystemMessage:
        return output.getvalue()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
