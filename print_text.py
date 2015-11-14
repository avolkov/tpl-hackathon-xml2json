#!/usr/bin/env python

## Collecting xml element tree events with  O(1) memory usage.
from xml.etree import cElementTree
import pickle


def iterate_over_xml(fname):
    #out_tags = set([])
    for _, elem in cElementTree.iterparse('tpl.xml'):
        if hasattr(elem, 'attrib') and elem.attrib:
            if 'NAME' in elem.attrib:
                print(elem.attrib['NAME'])
                import ipdb; ipdb.set_trace()
                print(elem.text)
            #import ipdb; ipdb.set_trace()
        elem.clear()
    #pickle.dump(out_tags, 'tpl_xml.tags')

if __name__ == "__main__":
    all_events = iterate_over_xml('tpl.xml')
    import ipdb; ipdb.set_trace()
