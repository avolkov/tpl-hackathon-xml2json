#!/usr/bin/env python

## Collecting xml element tree events with  O(1) memory usage.
from xml.etree import cElementTree
import pickle


def process_entries(record):
    import ipdb; ipdb.set_trace()


def iterate_over_xml(fname):
    #out_tags = set([])
    for _, elem in cElementTree.iterparse('tpl.xml'):
        if 'RECORD' in elem.__str__():
            process_entries(elem)
        elem.clear()
    #pickle.dump(out_tags, 'tpl_xml.tags')

if __name__ == "__main__":
    all_events = iterate_over_xml('tpl.xml')
    import ipdb; ipdb.set_trace()
