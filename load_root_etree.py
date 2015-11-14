#!/usr/bin/env python

## Collecting xml element tree events with  O(1) memory usage.
from xml.etree import cElementTree


def iterate_over_xml(fname):
    tree = cElementTree.parse('tpl.xml')
    root = tree.getroot()
    import ipdb; ipdb.set_trace()

if __name__ == "__main__":
    all_events = iterate_over_xml('tpl.xml')
    import ipdb; ipdb.set_trace()
