from panflute import *
import sys

headers = []


def header_warning(elem):
    if isinstance(elem, Header):
        if stringify(elem) in headers:
            sys.stderr.write("WARNING! REPEATED HEADER" + stringify(elem))
        else:
            headers.append(stringify(elem))


def change_header_level(elem, _):
    if isinstance(elem, Header) and elem.level > 2:
        return Header(Str(stringify(elem).upper()), level=elem.level)


def change_bold(file, _):
    file.replace_keyword("BOLD", Strong(Str("BOLD")))


if __name__ == "__main__":
    run_filters([header_warning, change_header_level], prepare=change_bold)
