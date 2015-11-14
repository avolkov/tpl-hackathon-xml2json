#!/usr/bin/env python

## Collecting xml element tree events with  O(1) memory usage.
from xml.etree import cElementTree


def collect_events(fname):
    out_events = {}
    for event, elem in cElementTree.iterparse('tpl.xml'):
        if event in out_events:
            out_events[event] += 1
        else:
            out_events[event] = 1
        elem.clear()
    return out_events

if __name__ == "__main__":
    all_events = collect_events('tpl.xml')
    import ipdb; ipdb.set_trace()
