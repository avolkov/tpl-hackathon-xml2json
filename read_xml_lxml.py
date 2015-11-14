#!/usr/bin/env python

from xml.etree import cElementTree

events = {}


def collect_events(fname):
    out_events = {}
    for event, elem in cElementTree.iterparse('tpl.xml'):
        if event in events:
            events[event] += 1
        else:
            events[event] = 1
        elem.clear()
    return out_events

if __name__ == "__main__":
    all_events = collect_events('tpl.xml')
