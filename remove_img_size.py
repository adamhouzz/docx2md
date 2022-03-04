#!/usr/bin/env python3

from panflute import *

def imageCleanUp(elem, doc):
    if isinstance(elem, Image):
        elem.attributes.pop('width', None)
        elem.attributes.pop('height', None)
    return elem


def main(doc=None):
    return run_filter(imageCleanUp, doc=doc)
if __name__ == "__main__":
    main()