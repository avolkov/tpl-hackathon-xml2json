#!/usr/bin/env python

## Collecting xml element tree events with  O(1) memory usage.
from xml.etree import cElementTree
import pickle


def iterate_over_xml(fname):
    out_tags = set([])
    for event, elem in cElementTree.iterparse('tpl.xml'):
        if elem.tag in out_tags:
            out_tags.add(elem.tag)
        elem.clear()
    with open('tpl_xml_tags.pkl', 'wb') as outfile:
        pickle.dump(out_tags, outfile)
    return out_tags

if __name__ == "__main__":
    all_tags = iterate_over_xml('tpl.xml')
    import ipdb; ipdb.set_trace()
